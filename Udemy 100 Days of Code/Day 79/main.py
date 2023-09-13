import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import geopandas as gpd
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
moving_average = prizes_won_per_year.rolling(window=5).mean()

plt.figure(figsize=(16,8), dpi=200)
plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks=np.arange(1900, 2021, step=5), 
           fontsize=14, 
           rotation=45)
 
ax = plt.gca() # get current axis
ax.set_xlim(1900, 2020)
 
ax.scatter(x=prizes_won_per_year.index, 
           y=prizes_won_per_year.values, 
           c='dodgerblue',
           alpha=0.7,
           s=100,)
 
ax.plot(prizes_won_per_year.index, 
        moving_average.values, 
        c='crimson', 
        linewidth=3,)
 
plt.show()

share_per_year = df_data.groupby('year').share_pct.mean()
share_moving_average = share_per_year.rolling(window=5).mean()

plt.figure(figsize=(16,8), dpi=200)
plt.title('Number of Nobel Prizes Awarded per Year', fontsize=18)
plt.yticks(fontsize=14)
plt.xticks(ticks=np.arange(1900, 2021, step=5), 
           fontsize=14, 
           rotation=45)
 
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_xlim(1900, 2020)
 
# Can invert axis
ax2.invert_yaxis()
 
ax1.scatter(x=prizes_won_per_year.index, 
           y=prizes_won_per_year.values, 
           c='dodgerblue',
           alpha=0.7,
           s=100,)
 
ax1.plot(prizes_won_per_year.index, 
        moving_average.values, 
        c='crimson', 
        linewidth=3,)
 
ax2.plot(prizes_won_per_year.index, 
        share_moving_average.values, 
        c='grey', 
        linewidth=3,)
 
plt.show()

top20_countries = df_data.groupby('birth_country_current').count().prize.sort_values(ascending=True).tail(20)
print(top20_countries)

top20_countries2 = df_data.groupby('birth_country').count().prize
print(top20_countries2)

top20_countries3 = df_data.groupby('organization_country').count().prize
print(top20_countries3)

h_bar = px.bar(x = top20_countries,
               y = top20_countries.index,
               orientation='h',
               color=top20_countries)

h_bar.update_layout(xaxis_title='Number of Prizes', yaxis_title='Countries')
 
h_bar.show()

top20_iso = df_data.groupby(['ISO'], as_index=False).agg({'prize': pd.Series.count})
print(top20_iso)

fig = px.choropleth(top20_iso, locations="ISO",
                    color="prize", # lifeExp is a column of gapminder
                    hover_name="ISO", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.matter)
fig.show()

country_per_category = df_data.groupby(['birth_country_current','category'], as_index=False).agg({'prize': pd.Series.count})
country_per_category.sort_values(by='prize', ascending=False, inplace=True)
print(country_per_category)

merged_df = pd.merge(country_per_category, top20_countries, on='birth_country_current')
merged_df.columns = ['birth_country_current', 'category', 'cat_prize', 'total_prize'] 
merged_df.sort_values(by='total_prize', inplace=True)
print(merged_df)

h_bar_split = px.bar(x = merged_df.cat_prize,
                     y = merged_df.birth_country_current,
                     color = merged_df.category,
                     title='Number of Prizes Awarded per Category',
                     orientation='h')
 
h_bar_split.update_layout(xaxis_title='Number of Prizes', 
                          yaxis_title='Countries')
h_bar_split.show()

country_over_time = df_data.groupby(['year','birth_country_current'], as_index=False).agg({'prize': pd.Series.count})

print(country_over_time)

cumulative_prizes = country_over_time.groupby(by=['birth_country_current',
                                              'year']).sum().groupby(level=[0]).cumsum()
cumulative_prizes.reset_index(inplace=True) 
print(cumulative_prizes)

l_chart = px.line(cumulative_prizes,
                  x='year', 
                  y='prize',
                  color='birth_country_current',
                  hover_name='birth_country_current')
 
l_chart.update_layout(xaxis_title='Year',
                      yaxis_title='Number of Prizes')
 
l_chart.show()

organisation_prizes = df_data.groupby(['organization_name'], as_index=False).agg({'prize': pd.Series.count})
organisation_prizes.sort_values(by='prize', inplace=True)
organisation_prizes = organisation_prizes[-20:]
print(organisation_prizes)

organisation_prizes_graph = px.bar(x=organisation_prizes.prize,
                                   y=organisation_prizes.organization_name,
                                   color=organisation_prizes.prize,
                                   hover_name=organisation_prizes.organization_name,
                                   orientation='h')

organisation_prizes_graph.show()


city_prizes = df_data.groupby(['organization_city'], as_index=False).agg({'prize': pd.Series.count})
city_prizes.sort_values(by='prize', inplace=True)
city_prizes = city_prizes[-20:]
print(city_prizes)

city_prizes_graph = px.bar(x=city_prizes.prize,
                                   y=city_prizes.organization_city,
                                   color=city_prizes.prize,
                                   hover_name=city_prizes.organization_city,
                                   orientation='h')

city_prizes_graph.show()

birth_city_prizes = df_data.groupby(['birth_city'], as_index=False).agg({'prize': pd.Series.count})
birth_city_prizes.sort_values(by='prize', inplace=True)
birth_city_prizes = birth_city_prizes[-20:]
print(birth_city_prizes)

birth_city_prizes_graph = px.bar(x=birth_city_prizes.prize,
                                 y=birth_city_prizes.birth_city,
                                 color=birth_city_prizes.prize,
                                 hover_name=birth_city_prizes.birth_city,
                                 orientation='h',
                                 color_continuous_scale=px.colors.sequential.Plasma)

birth_city_prizes_graph.show()


sun_df = df_data.groupby(['organization_country', 'organization_city', 'organization_name'], as_index=False).agg({'prize': pd.Series.count})

print(sun_df)

fig = px.sunburst(sun_df, path=['organization_country', 'organization_city', 'organization_name'], 
                    values='prize',
                    title='Where do Discoveries Take Place?',
                   )
 
fig.update_layout(xaxis_title='Number of Prizes', 
                    yaxis_title='City',
                    coloraxis_showscale=False)
 
fig.show()

df_data['year'] = pd.to_datetime(df_data['year'], format='%Y')
df_data['year'] = df_data['year'].dt.year
df_data['birth_date'] = df_data['birth_date'].dt.year
df_data['winning_age'] = df_data['year'].subtract(df_data['birth_date'])

winner_age = df_data.groupby(['full_name', 'winning_age'], as_index=False).agg({'prize': pd.Series.count})
df_data.sort_values('winning_age', inplace=True, ascending=False)

sns.histplot(data=df_data,
             x=df_data.winning_age,
             bins=30)
plt.xlabel('Age')
plt.title('Distribution of Age on Receipt of Prize')
plt.show()

plt.figure(figsize=(8,4), dpi=200)
with sns.axes_style("whitegrid"):
    sns.regplot(data=df_data,
                x='year',
                y='winning_age',
                lowess=True, 
                scatter_kws = {'alpha': 0.4},
                line_kws={'color': 'black'})
 
plt.show()

plt.figure(figsize=(8,4), dpi=200)
sns.boxplot(data=df_data,
                x='category',
                y='winning_age',
               )
plt.show()

with sns.axes_style('whitegrid'):
    sns.lmplot(data=df_data,
               x='year', 
               y='winning_age',
               row = 'category',
               lowess=True, 
               aspect=2,
               scatter_kws = {'alpha': 0.6},
               line_kws = {'color': 'black'},)
 
plt.show()

with sns.axes_style("whitegrid"):
    sns.lmplot(data=df_data,
               x='year',
               y='winning_age',
               hue='category',
               lowess=True, 
               aspect=2,
               scatter_kws={'alpha': 0.5},
               line_kws={'linewidth': 5})
plt.show()