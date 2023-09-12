import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

df_data = pd.read_csv('C:/Users/RSiu9/OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 79/nobel_prize_data.csv')

# check shape of dataframe
print(df_data.shape)

# check column names and datatype of dataframe
print(df_data.info())

# check if any duplicated values
print(df_data.duplicated().values.any())
duplicated_rows = df_data[df_data.duplicated()]
print(len(duplicated_rows))

# check if any na values
print(df_data.isna().values.any())

for col in df_data.columns:
    print(f"number of NaNs in {col} row: {len(df_data[df_data[col].isna()==True])}")
# or just use df_data.isna().sum()    

df_data['birth_date'] = pd.to_datetime(df_data['birth_date'])
separated_values = df_data.prize_share.str.split('/', expand=True)
numerator = pd.to_numeric(separated_values[0])
denomenator = pd.to_numeric(separated_values[1])
df_data['share_pct'] = numerator / denomenator

print(df_data.info())

genders = df_data.sex.value_counts()
fig = px.pie(labels=genders.index,
            values=genders.values,
            title="Nobel Prize Winners by Gender",
            names=genders.index,
            hole=0.6,
            )

fig.update_traces(textposition='outside', textinfo='percent+label')
 
fig.show()

print(df_data.sort_values('year')[df_data.sex == "Female"][:3])

print(df_data.full_name.duplicated().values.any())
duplicated_names = df_data.full_name[df_data.full_name.duplicated()]
print(duplicated_names)

print(df_data.category.unique())

prizes_per_category = df_data.category.value_counts()
v_bar = px.bar(
        x = prizes_per_category.index,
        y = prizes_per_category.values,
        color = prizes_per_category.values,
        color_continuous_scale='Aggrnyl',
        title='Number of Prizes Awarded per Category')
 
v_bar.update_layout(xaxis_title='Nobel Prize Category', 
                    coloraxis_showscale=False,
                    yaxis_title='Number of Prizes')
v_bar.show()
 
print(df_data.sort_values('year')[df_data.category == "Economics"]['full_name'])

df_men_vs_women = df_data.groupby(['category', 'sex'], as_index=False).agg({'prize': pd.Series.count})
print(df_men_vs_women)

df_men_vs_women.sort_values('prize', ascending=False, inplace=True)
v_bar_split = px.bar(x = df_men_vs_women.category,
                     y = df_men_vs_women.prize,
                     color = df_men_vs_women.sex,
                     title='Number of Prizes Awarded per Category split by Men and Women')
 
v_bar_split.update_layout(xaxis_title='Nobel Prize Category', 
                          yaxis_title='Number of Prizes')
v_bar_split.show()

prizes_won_per_year = df_data.groupby('year').agg({'prize': pd.Series.count})
print(prizes_won_per_year)
rolling_prizes = prizes_won_per_year.rolling(window=5).mean()

plt.title('Prizes Won per Year')
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Prizes', fontsize=14)
plt.ylim(0, 35000)

plt.plot(rolling_prizes.index, rolling_prizes.values)
plt.legend(fontsize=8) 