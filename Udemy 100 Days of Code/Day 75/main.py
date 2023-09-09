#%%
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
import matplotlib.dates as mdates

register_matplotlib_converters()

bitcoin_search = pd.read_csv('C:/Users/RSiu9/OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 75/data/Bitcoin Search Trend.csv')
bitcoin_daily = pd.read_csv('C:/Users/RSiu9/OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 75/data/Daily Bitcoin Price.csv')
tesla_search = pd.read_csv('C:/Users/RSiu9/OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 75/data/TESLA Search Trend vs Price.csv')
ue_old = pd.read_csv('C:/Users/RSiu9/OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 75/data/UE Benefits Search vs UE Rate 2004-19.csv')
ue_new = pd.read_csv('C:/Users/RSiu9/OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 75/data/UE Benefits Search vs UE Rate 2004-20.csv')

print(bitcoin_search.shape, bitcoin_daily.shape, tesla_search.shape, ue_old.shape, ue_new.shape)

print(bitcoin_search.describe())
print(bitcoin_daily.describe())
print(tesla_search.describe())
print(ue_old.describe())
print(ue_new.describe())

print(f"Any missing values for tesla?: {tesla_search.isna().values.any()}")
print(f"Any missing values for bitcoin?: {bitcoin_search.isna().values.any()}")
print(f"Any missing values for UE?: {ue_new.isna().values.any()}")
print(f"Any missing values for daily btc?: {bitcoin_daily.isna().values.any()}")

print(f"total missing values: {bitcoin_daily.isna().values.sum()}")
print(bitcoin_daily[bitcoin_daily['CLOSE'].isna()])

bitcoin_daily.dropna(inplace=True)
print(f"Any missing values for daily btc?: {bitcoin_daily.isna().values.any()}")

# Convert date into datetime format
bitcoin_search['MONTH'] = pd.to_datetime(bitcoin_search['MONTH'])
bitcoin_daily['DATE'] = pd.to_datetime(bitcoin_daily['DATE'])
tesla_search['MONTH'] = pd.to_datetime(tesla_search['MONTH'])
ue_old['MONTH'] = pd.to_datetime(ue_old['MONTH'])
ue_new['MONTH'] = pd.to_datetime(ue_new['MONTH'])

bitcoin_monthly = bitcoin_daily.resample('M', on='DATE').last()
print(bitcoin_monthly)

years = mdates.YearLocator()
months = mdates. MonthLocator()
years_format = mdates.DateFormatter('%Y')

# Plotting
plt.figure(figsize=(14,8), dpi=200)
plt.title('Tesla Web Search vs Price', fontsize=18)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('TSLA Stock Price', color = 'r', fontsize=14)
ax1.set_ylim([0, 600])
ax1.set_xlim([tesla_search.MONTH.min(), tesla_search.MONTH.max()])
ax1.plot(tesla_search.MONTH, tesla_search.TSLA_USD_CLOSE, 'r', linewidth=2)

ax2.set_ylabel('Search Trend', color = 'skyblue', fontsize=14)
ax2.plot(tesla_search.MONTH, tesla_search.TSLA_WEB_SEARCH, 'skyblue', linewidth=2)

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_format)
ax1.xaxis.set_minor_locator(months)

plt.show()

# Plotting
plt.figure(figsize=(14,8), dpi=200)
plt.title('Bitcoin News Search vs Resampled Price', fontsize=18)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('BTC Price', color = 'orange', fontsize=14)
ax1.set_ylim([0, 15000])
ax1.set_xlim([bitcoin_monthly.index.min(), bitcoin_monthly.index.max()])
ax1.plot(bitcoin_monthly.index, bitcoin_monthly.CLOSE, color='orange', linewidth=2, linestyle = '--')

ax2.set_ylabel('Search Trend', color = 'skyblue', fontsize=14)
ax2.plot(bitcoin_monthly.index, bitcoin_search.BTC_NEWS_SEARCH, 'skyblue', linewidth=2)

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_format)
ax1.xaxis.set_minor_locator(months)

plt.show()


# Plotting
plt.figure(figsize=(14,8), dpi=200)
plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
plt.xticks(fontsize=14, rotation=45)
plt.grid(color='grey', linestyle='--')

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('FRED U/E Rate', color = 'purple', fontsize=14)
ax1.set_ylim(bottom=3, top=10.5)
ax1.set_xlim([ue_old.MONTH.min(), ue_old.MONTH.max()])
ax1.plot(ue_old.MONTH, ue_old.UNRATE, color='purple', linewidth=2, linestyle = '--')

ax2.set_ylabel('Search Trend', color = 'skyblue', fontsize=14)
ax2.plot(ue_old.MONTH, ue_old.UE_BENEFITS_WEB_SEARCH, 'skyblue', linewidth=2)

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_format)
ax1.xaxis.set_minor_locator(months)

plt.show()

# Plotting
plt.figure(figsize=(14,8), dpi=200)
plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
plt.xticks(fontsize=14, rotation=45)
plt.grid(color='grey', linestyle='--')

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('FRED U/E Rate', color = 'purple', fontsize=14)
ax1.set_ylim(bottom=3, top=15)
ax1.set_xlim([ue_new.MONTH.min(), ue_new.MONTH.max()])
ax1.plot(ue_new.MONTH, ue_new.UNRATE, color='purple', linewidth=2, linestyle = '--')

ax2.set_ylabel('Search Trend', color = 'skyblue', fontsize=14)
ax2.plot(ue_new.MONTH, ue_new.UE_BENEFITS_WEB_SEARCH, 'skyblue', linewidth=2)

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_format)
ax1.xaxis.set_minor_locator(months)

plt.show()


# %%
