import pandas as pd
import numpy as np

import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

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

# Pairplot of All data
#pair_plot = sns.pairplot(data)
#plt.show()

# Join Plot of DIS v NOX
with sns.axes_style('darkgrid'):
    dis_v_nox = sns.jointplot(data = data,
                            x = data.DIS,
                            y = data.NOX,
                            height=8, 
                            kind='scatter',
                            color='deeppink', 
                            joint_kws={'alpha':0.5})
    
plt.show()

# Join Plot of INDUS v NOX
with sns.axes_style('darkgrid'):
    dis_v_nox = sns.jointplot(data = data,
                            x = data.NOX,
                            y = data.INDUS,
                            height=8, 
                            kind='scatter',
                            color='skyblue', 
                            joint_kws={'alpha':0.8})
    
plt.show()

# Join Plot of LSTAT vs RM
with sns.axes_style('darkgrid'):
    dis_v_nox = sns.jointplot(data = data,
                            x = data.LSTAT,
                            y = data.RM,
                            height=8, 
                            kind='scatter',
                            color='darkgreen', 
                            joint_kws={'alpha':0.5})
    
plt.show()

# Join Plot of LSTAT vs PRICE
with sns.axes_style('darkgrid'):
    dis_v_nox = sns.jointplot(data = data,
                            x = data.LSTAT,
                            y = data.PRICE,
                            height=8, 
                            kind='scatter',
                            color='red', 
                            joint_kws={'alpha':0.8})
    
plt.show()

# Join Plot of RM vs PRICE
with sns.axes_style('darkgrid'):
    dis_v_nox = sns.jointplot(data = data,
                            x = data.RM,
                            y = data.PRICE,
                            height=8, 
                            kind='scatter',
                            color='purple', 
                            joint_kws={'alpha':0.3})
    
plt.show()

X, y = data.drop('PRICE', axis = 1), data.PRICE

X_train, X_test, y_train, y_test = train_test_split(
           X, y, test_size=0.2, random_state=10)

# % of training set
train_pct = 100*len(X_train)/len(X)
print(f'Training data is {train_pct:.3}% of the total data.')

# % of test data set
test_pct = 100*X_test.shape[0]/X.shape[0]
print(f'Test data makes up the remaining {test_pct:0.3}%.')

# Run a linear regression on the training set
regression = LinearRegression()
regression.fit(X, y)
rsquared = regression.score(X_train, y_train)

# print rsquared value
print(f'Training data r-squared: {rsquared:.2}')

# Print the intercept and coefficients
print(f"The regression intercept is: {regression.intercept_}")
for coeff in range(len(regression.coef_)):
    print(f"{X.columns[coeff]}'s coefficient is {regression.coef_[coeff]}")
# regr_coef = pd.DataFrame(data=regression.coef_, index=X_train.columns, columns=['Coefficient'])
# print(regr_coef)

predicted_values = regression.predict(X_train)
residuals = (y_train - predicted_values)

# Original Regression of Actual vs. Predicted Prices
plt.figure(dpi=100)
plt.scatter(x=y_train, y=predicted_values, c='indigo', alpha=0.6)
plt.plot(y_train, y_train, color='cyan')
plt.title(f'Actual vs Predicted Prices: $y _i$ vs $\hat y_i$', fontsize=17)
plt.xlabel('Actual prices 000s $y _i$', fontsize=14)
plt.ylabel('Prediced prices 000s $\hat y _i$', fontsize=14)
plt.show()

# Residuals vs Predicted values
plt.figure(dpi=100)
plt.scatter(x=predicted_values, y=residuals, c='indigo', alpha=0.6)
plt.title('Residuals vs Predicted Values', fontsize=17)
plt.xlabel('Predicted Prices $\hat y _i$', fontsize=14)
plt.ylabel('Residuals', fontsize=14)
plt.show()

resid_mean = round(residuals.mean(), 2)
resid_skew = round(residuals.skew(), 2)
print(f"Residual mean: {resid_mean}")
print(f"Residual skew: {resid_skew}")

residual_dist = sns.displot(data = residuals,
                            x = residuals.values,
                            bins = 50,
                            aspect = 2,
                            kde = True,
                            )

plt.title(f'Distribution of Residual Price')
plt.xlabel('Price in 000s')
plt.ylabel('Nr. of Homes')
plt.show()

# Plot the normal prices
data_price_skew = data.PRICE.skew()
data_price_dist = sns.displot(data.PRICE, kde = True, color='green')
plt.title(f'Normal Prices. Skew is {data_price_skew:.3}')
plt.show()

# Convert and Plot the log of the prices
#data['log_prices'] = np.log(data.PRICE)

data_log_skew = np.log(data.PRICE).skew()
data_log_dist = sns.displot(np.log(data.PRICE), kde = True, color='green')
plt.title(f'Log Prices. Skew is {data_log_skew:.3}')
plt.show()

# Graph log price vs original price
plt.figure(dpi=150)
plt.scatter(data.PRICE, np.log(data.PRICE))

plt.title('Mapping the Original Price to a Log Price')
plt.ylabel('Log Price')
plt.xlabel('Actual $ Price in 000s')
plt.show()

# check coefficients and linear regression of log prices
new_target = np.log(data['PRICE']) # Use log prices
features = data.drop('PRICE', axis=1)

X_train, X_test, log_y_train, log_y_test = train_test_split(features, 
                                                    new_target, 
                                                    test_size=0.2, 
                                                    random_state=10)

log_regr = LinearRegression()
log_regr.fit(X_train, log_y_train)
log_rsquared = log_regr.score(X_train, log_y_train)

log_predictions = log_regr.predict(X_train)
log_residuals = (log_y_train - log_predictions)

print(f'Training data r-squared: {log_rsquared:.2}')

df_coef = pd.DataFrame(data=log_regr.coef_, index=X_train.columns, columns=['coef'])
print(df_coef)

# Graph of Actual vs. Predicted Log Prices
plt.scatter(x=log_y_train, y=log_predictions, c='navy', alpha=0.6)
plt.plot(log_y_train, log_y_train, color='cyan')
plt.title(f'Actual vs Predicted Log Prices: $y _i$ vs $\hat y_i$ (R-Squared {log_rsquared:.2})', fontsize=17)
plt.xlabel('Actual Log Prices $y _i$', fontsize=14)
plt.ylabel('Prediced Log Prices $\hat y _i$', fontsize=14)
plt.show()

# Original Regression of Actual vs. Predicted Prices
plt.scatter(x=y_train, y=predicted_values, c='indigo', alpha=0.6)
plt.plot(y_train, y_train, color='cyan')
plt.title(f'Original Actual vs Predicted Prices: $y _i$ vs $\hat y_i$ (R-Squared {rsquared:.3})', fontsize=17)
plt.xlabel('Actual prices 000s $y _i$', fontsize=14)
plt.ylabel('Prediced prices 000s $\hat y _i$', fontsize=14)
plt.show()

# Residuals vs Predicted values (Log prices)
plt.scatter(x=log_predictions, y=log_residuals, c='navy', alpha=0.6)
plt.title('Residuals vs Fitted Values for Log Prices', fontsize=17)
plt.xlabel('Predicted Log Prices $\hat y _i$', fontsize=14)
plt.ylabel('Residuals', fontsize=14)
plt.show()

# Residuals vs Predicted values
plt.scatter(x=predicted_values, y=residuals, c='indigo', alpha=0.6)
plt.title('Original Residuals vs Fitted Values', fontsize=17)
plt.xlabel('Predicted Prices $\hat y _i$', fontsize=14)
plt.ylabel('Residuals', fontsize=14)
plt.show()

# Distribution of Residuals (log prices) - checking for normality
log_resid_mean = round(log_residuals.mean(), 2)
log_resid_skew = round(log_residuals.skew(), 2)

sns.displot(log_residuals, kde=True, color='navy')
plt.title(f'Log price model: Residuals Skew ({log_resid_skew}) Mean ({log_resid_mean})')
plt.show()

sns.displot(residuals, kde=True, color='indigo')
plt.title(f'Original model: Residuals Skew ({resid_skew}) Mean ({resid_mean})')
plt.show()

print(f'Original Model Test Data r-squared: {regression.score(X_test, y_test):.2}')
print(f'Log Model Test Data r-squared: {log_regr.score(X_test, log_y_test):.2}')

# Average Values in the Dataset
features = data.drop(['PRICE'], axis=1)
average_vals = features.mean().values
property_stats = pd.DataFrame(data=average_vals.reshape(1, len(features.columns)), 
                              columns=features.columns)
print(property_stats)

# Make prediction
log_estimate = log_regr.predict(property_stats)[0]
print(f'The log price estimate is ${log_estimate:.3}')

# Convert Log Prices to Acutal Dollar Values
dollar_est = np.e**log_estimate * 1000
# or use
dollar_est = np.exp(log_estimate) * 1000
print(f'The property is estimated to be worth ${dollar_est:.6}')

# Define Property Characteristics
next_to_river = True
nr_rooms = 8
students_per_classroom = 20 
distance_to_town = 5
pollution = data.NOX.quantile(q=0.75) # high
amount_of_poverty =  data.LSTAT.quantile(q=0.25) # low

# Set Property Characteristics
property_stats['RM'] = nr_rooms
property_stats['PTRATIO'] = students_per_classroom
property_stats['DIS'] = distance_to_town

if next_to_river:
    property_stats['CHAS'] = 1
else:
    property_stats['CHAS'] = 0

property_stats['NOX'] = pollution
property_stats['LSTAT'] = amount_of_poverty

# Make prediction
log_estimate = log_regr.predict(property_stats)[0]
print(f'The log price estimate is ${log_estimate:.3}')

# Convert Log Prices to Acutal Dollar Values
dollar_est = np.e**log_estimate * 1000
print(f'The property is estimated to be worth ${dollar_est:.6}')