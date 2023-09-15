import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


df_monthly = pd.read_csv('C:/Users/RSiu9/OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 80/monthly_deaths.csv')
df_yearly = pd.read_csv('C:/Users/RSiu9/OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 80/annual_deaths_by_clinic.csv')

# check shape of dfs
print(f"Shape of yearly df: {df_yearly.shape}")
print(f"Shape of monthly df: {df_monthly.shape}")

# get column names
print("Monthly DF Column Names\n", df_monthly.info())
print("Yearly DF Column Names\n", df_yearly.info())

# check for NaNs
print(f"NaNs in Monthly DF: {df_monthly.isna().values.any()}")
print(f"NaNs in Yearly DF: {df_yearly.isna().values.any()}")

# check for duplicates
print(f"Duplicates in Monthly DF: {df_monthly.duplicated().values.any()}")
print(f"Duplicates in Yearly DF: {df_yearly.duplicated().values.any()}")

# check averages
print("Monthly DF Info\n", df_monthly.describe())
print("Yearly DF Info\n", df_yearly.describe())

# percentage of women dying in child birth
print("By year\n", df_yearly['deaths']/df_yearly['births'] * 100)
print(f"Chances of dying in the 1840s in Vienna: {df_yearly['deaths'].sum() / df_yearly['births'].sum() * 100:.3}%")

df_monthly.date = pd.to_datetime(df_monthly.date)

years = mdates.YearLocator()
months = mdates. MonthLocator()
years_format = mdates.DateFormatter('%Y') 

plt.figure(figsize=(14,8), dpi=200)
plt.title('Total Number of Monthly Births and Deaths', fontsize=18)
 
ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_xlim([df_monthly.date.min(), df_monthly.date.max()])
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_format)
ax1.xaxis.set_minor_locator(months)
 
ax1.grid(color='grey', linestyle='--')
 
ax1.plot(df_monthly['date'], 
         df_monthly['births'], 
         color='skyblue', 
         linewidth=3)
 
ax2.plot(df_monthly['date'], 
         df_monthly['deaths'], 
         color='crimson', 
         linewidth=2, 
         linestyle='--')
 
plt.show()