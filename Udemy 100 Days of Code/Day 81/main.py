import pandas as pd
import numpy as np

import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

# set pandas display of floats to 2 decimal places
pd.options.display.float_format = '{:,.2f}'.format

data = pd.read_csv('C:/Users/RSiu9/OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 81/boston.csv', index_col = 0)

'''
Attribute Information (in order):
    1. CRIM     per capita crime rate by town
    2. ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
    3. INDUS    proportion of non-retail business acres per town
    4. CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
    5. NOX      nitric oxides concentration (parts per 10 million)
    6. RM       average number of rooms per dwelling
    7. AGE      proportion of owner-occupied units built prior to 1940
    8. DIS      weighted distances to five Boston employment centres
    9. RAD      index of accessibility to radial highways
    10. TAX      full-value property-tax rate per $10,000
    11. PTRATIO  pupil-teacher ratio by town
    12. B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
    13. LSTAT    % lower status of the population
    14. PRICE     Median value of owner-occupied homes in $1000's
'''

# get shape of data
print(f"Shape of data: {data.shape}")
print(f"Num Rows in Data:{data.shape[0]}\nNum Cols in Data:{data.shape[1]}")

# check for column names
print(data.info())

# check for NaN and Duplicate Values
print(f"Any NaNs? {data.isna().values.any()}")
print(f"Any Duplicates? {data.duplicated().values.any()}")

# Average Students per teacher
ptratio_mean = data['PTRATIO'].describe()['mean']
print(f"The average students per teacher ratio: {ptratio_mean:.2f}")

# Average Price of Home
price_mean = data['PRICE'].describe()['mean']
print(f"The average house price: {price_mean:.2f} Thousand")

# CHAS Feature
# CHAS - Charles River dummy variable, used to determine if the houses are close to the Charles River as it's possible this influences house prices.
chas_max = data['CHAS'].describe()['max']
chas_min = data['CHAS'].describe()['min']
print(f"The CHAS max is: {chas_max:.2f}\nThe CHAS min is: {chas_min:.2f}")

# Room information
max_rooms = data['RM'].describe()['max']
min_rooms = data['RM'].describe()['min']
print(f"The maximum number of rooms in a dwelling is: {max_rooms:.2f}\nThe minimum number of rooms in a dwelling is: {min_rooms:.2f}")

# Plot Housing Prices
price_dist = sns.displot(data = data,
                         x = data.PRICE,
                         bins = 50,
                         aspect = 2,
                         kde = True,
                         )

plt.title(f'1970s Home Values in Boston. Average: ${(1000*data.PRICE.mean()):.6}')
plt.xlabel('Price in 000s')
plt.ylabel('Nr. of Homes')
plt.show()

# Plot Number of Rooms
rooms_dist = sns.displot(data = data,
                         x = data.RM,
                         bins = 50,
                         aspect = 2,
                         kde = True,
                         )

plt.title(f'1970s Number of Rooms per House in Boston.')
plt.xlabel('Number of Rooms')
plt.ylabel('Number of Homes')
plt.show()

# Plot weighted distances to five Boston employment centres
dis_dist = sns.displot(data = data,
                       x = data["DIS"],
                       bins = 50,
                       aspect = 2,
                       kde = True,
)

plt.title('1970s Housing Weighted Distance to Five Boston Employment Centres')
plt.xlabel('Weighted Distance')
plt.ylabel('Number of Homes')
plt.show()

# Plot index of accessibility to radial highways
rad_dist = sns.displot(data = data,
                       x = data["RAD"],
                       bins = 50,
                       aspect = 2,
                       kde = True,
)

plt.title('1970s Housing Index of Accessibility to Radial Highways')
plt.xlabel('Index')
plt.ylabel('Number of Homes')
plt.show()

# Plot index of accessibility to radial highways
river_access = data['CHAS'].value_counts()

bar = px.bar(x=['No', 'Yes'],
             y=river_access.values,
             color=river_access.values,
             color_continuous_scale=px.colors.sequential.haline,
             title='Next to Charles River?')

bar.update_layout(xaxis_title='Property Located Next to the River?', 
                  yaxis_title='Number of Homes',
                  coloraxis_showscale=False)
bar.show()

pair_plot = sns.pairplot(data)
plt.show()