#%%
import numpy as np
import pandas as pd

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
