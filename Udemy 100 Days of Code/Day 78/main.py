#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


cost_df = pd.read_csv('C:/Users/RSiu9/OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 78/cost_revenue_dirty.csv')

print(cost_df.shape)
print(cost_df.isna().values.any())
print(cost_df.duplicated().values.any())
#duplicated_rows = cost_df[cost_df.duplicated()]
#print(len(duplicated_rows))


data_to_update = ['USD_Production_Budget', 'USD_Worldwide_Gross', 'USD_Domestic_Gross']

for data in data_to_update:
    cost_df[data] = cost_df[data].astype(str).str.replace(',', "")
    cost_df[data] = cost_df[data].astype(str).str.replace('$', "")
    cost_df[data] = pd.to_numeric(cost_df[data])

cost_df['Release_Date'] = pd.to_datetime(cost_df['Release_Date'])
print("\n next challenges")
print("c1, 1")
print(cost_df['USD_Production_Budget'].mean())
#print(cost_df.groupby('USD_Production_Budget').mean())
print("c1, 2")
print(cost_df['USD_Worldwide_Gross'].mean())

print("c1, 3")
print(cost_df.sort_values('USD_Worldwide_Gross', ascending=False).tail())
print(cost_df.sort_values('USD_Domestic_Gross', ascending=False).tail())

print("c1, 4")
print(cost_df.sort_values('USD_Production_Budget').head())
print(cost_df.sort_values('USD_Worldwide_Gross').head())

print("c1, 5")
print(cost_df.sort_values('USD_Production_Budget')['USD_Worldwide_Gross'])
print(cost_df.sort_values('USD_Production_Budget', ascending=False)['USD_Worldwide_Gross'])

print("c2")
print(cost_df[cost_df['USD_Domestic_Gross'] == 0])
a = cost_df[cost_df['USD_Domestic_Gross'] == 0]
print(a.sort_values('USD_Production_Budget', ascending=False))

print("c3")
print(cost_df[cost_df['USD_Domestic_Gross'] == 0])
a = cost_df[cost_df['USD_Domestic_Gross'] == 0]
print(a.sort_values('USD_Production_Budget', ascending=False))

print("Challenge")

# Using the .query() function to filter on multiple conditions
# 0 revenue domestically but generated revenue oversease
print(cost_df.query('USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0').tail())

# date of data collection
scrape_date = pd.Timestamp('2018-5-1')

future_releases = cost_df[cost_df.Release_Date >= scrape_date]
print(future_releases.shape)

data_clean = cost_df.drop(future_releases.index)
print(data_clean.shape)

money_losing = data_clean.query('USD_Production_Budget > USD_Worldwide_Gross')
money_losing.shape[0]/data_clean.shape[0]

print(money_losing.shape[0]/data_clean.shape[0])

plt.figure(figsize=(8,4), dpi=200)
 
ax = sns.scatterplot(data=data_clean,
                     x='USD_Production_Budget', 
                     y='USD_Worldwide_Gross')
 
ax.set(ylim=(0, 3000000000),
       xlim=(0, 450000000),
       ylabel='Revenue in $ billions',
       xlabel='Budget in $100 millions')
 
plt.show()

plt.figure(figsize=(8,4), dpi=200)
ax = sns.scatterplot(data=data_clean,
                     x='USD_Production_Budget', 
                     y='USD_Worldwide_Gross',
                     hue='USD_Worldwide_Gross', # colour
                     size='USD_Worldwide_Gross',) # dot size
 
ax.set(ylim=(0, 3000000000),
       xlim=(0, 450000000),
       ylabel='Revenue in $ billions',
       xlabel='Budget in $100 millions',)
 
plt.show()

plt.figure(figsize=(8,4), dpi=200)
 
# set styling on a single chart
with sns.axes_style('darkgrid'):
  ax = sns.scatterplot(data=data_clean,
                       x='USD_Production_Budget', 
                       y='USD_Worldwide_Gross',
                       hue='USD_Worldwide_Gross',
                       size='USD_Worldwide_Gross')
 
  ax.set(ylim=(0, 3000000000),
        xlim=(0, 450000000),
        ylabel='Revenue in $ billions',
        xlabel='Budget in $100 millions')
  
  plt.show()


with sns.axes_style('darkgrid'):
    plt.figure(figsize=(8,4), dpi=200)
    ax = sns.scatterplot(data=data_clean,
                        x='Release_Date', 
                        y='USD_Production_Budget',
                        hue='USD_Worldwide_Gross', # colour
                        size='USD_Worldwide_Gross',) # dot size
    
    ax.set(ylim=(0, 450000000),
        xlim=(data_clean.Release_Date.min(), data_clean.Release_Date.max()),
        ylabel='Budget in $100 millions',
        xlabel='Year',)
    
    plt.show()

dates = pd.DatetimeIndex(data_clean['Release_Date'])
decades = dates.year // 10*10
#print(decades)
data_clean['Decade'] = decades
#print(data_clean)

old_films = data_clean[data_clean.Decade <= 1960]
new_films = data_clean[data_clean.Decade > 1960]

plt.figure(figsize=(8,4), dpi=200)
with sns.axes_style("whitegrid"):
  sns.regplot(data=old_films, 
            x='USD_Production_Budget', 
            y='USD_Worldwide_Gross',
            scatter_kws = {'alpha': 0.4},
            line_kws = {'color': 'black'})
plt.show()

plt.figure(figsize=(8,4), dpi=200)
with sns.axes_style("darkgrid"):
  ax = sns.regplot(data=new_films, 
            x='USD_Production_Budget', 
            y='USD_Worldwide_Gross',
            color = '#2f4b7c',
            scatter_kws = {'alpha': 0.3},
            line_kws = {'color': '#ff7c43'})
  ax.set(ylim=(0, 3000000000),
        xlim=(0, 450000000),
        ylabel='Budget in $ millions',
        xlabel='Revenue in $ billions')
plt.show()

regression = LinearRegression()

# Explanatory Variable(s) or Feature(s)
X = pd.DataFrame(new_films, columns=['USD_Production_Budget'])
 
# Response Variable or Target
y = pd.DataFrame(new_films, columns=['USD_Worldwide_Gross']) 

# Find the best-fit line
regression.fit(X, y)
print(regression.intercept_) # y-intercept
print(regression.coef_) # gradient

# R-squared
regression.score(X, y)

# Explanatory Variable(s) or Feature(s)
old_X = pd.DataFrame(old_films, columns=['USD_Production_Budget'])
 
# Response Variable or Target
old_y = pd.DataFrame(old_films, columns=['USD_Worldwide_Gross']) 

# Find the best-fit line
regression.fit(old_X, old_y)
print(regression.intercept_) # y-intercept
print(regression.coef_) # gradient

# R-squared
regression.score(old_X, old_y)

budget = 350000000
revenue_estimate = regression.intercept_[0] + regression.coef_[0,0]*budget
revenue_estimate = round(revenue_estimate, -6)
print(f'The estimated revenue for a $350 film is around ${revenue_estimate:.10}.')
# %%
