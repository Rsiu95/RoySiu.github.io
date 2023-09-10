#%%
import pandas
import plotly.express as px


apps_df = pandas.read_csv('C:/Users/RSiu9/OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 76/data/apps.csv')


apps_df = apps_df.drop(columns = ['Last_Updated','Android_Ver'])
print(apps_df.isna().values.any())
cleaned_app_df = apps_df.dropna()

print(cleaned_app_df)
duplicated_rows = cleaned_app_df[cleaned_app_df.duplicated()]
print(cleaned_app_df[cleaned_app_df.App == 'Instagram'])

cleaned_app_df = cleaned_app_df.drop_duplicates(subset=['App', 'Type', 'Price'])
print(cleaned_app_df[cleaned_app_df.App == 'Instagram'])


print(cleaned_app_df["Rating"].idxmax())
print(cleaned_app_df.loc[21])

print(cleaned_app_df.loc[cleaned_app_df['Size_MBs'].idxmax()])

print(cleaned_app_df.sort_values('Reviews', ascending=False).head(50)[cleaned_app_df.sort_values('Reviews', ascending=False).head(50).Type == 'Paid'])

ratings = cleaned_app_df.Content_Rating.value_counts()
fig = px.pie(labels=ratings.index,
values=ratings.values,
title="Content Rating",
names=ratings.index,
hole=0.6,
)
fig.update_traces(textposition='outside', textinfo='percent+label')
 
fig.show()

print(cleaned_app_df.Installs)
cleaned_app_df['Installs'] = cleaned_app_df.Installs.astype(str).str.replace(',', "")
cleaned_app_df['Installs']  = pandas.to_numeric(cleaned_app_df['Installs'])
print(cleaned_app_df[['App', 'Installs']].groupby('Installs').count())

cleaned_app_df['Price'] = cleaned_app_df.Price.astype(str).str.replace('$', "")
cleaned_app_df['Price']  = pandas.to_numeric(cleaned_app_df['Price'])
print(cleaned_app_df['Price'])

cleaned_app_df['Revenue_Estimate'] = cleaned_app_df.Installs.mul(cleaned_app_df.Price)
print(cleaned_app_df.sort_values('Revenue_Estimate', ascending=False)[:10])

print(cleaned_app_df.Category.nunique())
top10_category = cleaned_app_df.Category.value_counts()[:10]
print(top10_category)

bar = px.bar(x = top10_category.index, # index = category name
             y = top10_category.values)
 
bar.show()

category_installs = cleaned_app_df.groupby('Category').agg({'Installs': pandas.Series.sum})
category_installs.sort_values('Installs', ascending=True, inplace=True)

h_bar = px.bar(x = category_installs.Installs,
               y = category_installs.index,
               orientation='h')

h_bar.update_layout(xaxis_title='Number of Downloads', yaxis_title='Category')
 
h_bar.show()

# num apps per category
cat_number = cleaned_app_df.groupby('Category').agg({'App': pandas.Series.count})

# merge num apps per category with num installs per category
cat_merged_df = pandas.merge(cat_number, category_installs, on='Category', how="inner")

print(f'The dimensions of the DataFrame are: {cat_merged_df.shape}')
cat_merged_df.sort_values('Installs', ascending=False)

scatter = px.scatter(cat_merged_df, # data
                    x='App', # column name
                    y='Installs',
                    title='Category Concentration',
                    size='App',
                    hover_name=cat_merged_df.index,
                    color='Installs')
 
scatter.update_layout(xaxis_title="Number of Apps (Lower=More Concentrated)",
                      yaxis_title="Installs",
                      yaxis=dict(type='log'))
 
scatter.show()

stack = cleaned_app_df.Genres.str.split(';', expand=True).stack()
print(f'We now have a single column with shape: {stack.shape}')
num_genres = stack.value_counts()
print(f'Number of genres: {len(num_genres)}')

bar = px.bar(x = num_genres.index[:15], # index = category name
             y = num_genres.values[:15], # count
             title='Top Genres',
             hover_name=num_genres.index[:15],
             color=num_genres.values[:15],
             color_continuous_scale='Agsunset')
 
bar.update_layout(xaxis_title='Genre',
yaxis_title='Number of Apps',
coloraxis_showscale=False)
 
bar.show()

print(cleaned_app_df.Type.value_counts())

#as_index = false to apply to columns rather than index
df_free_vs_paid = cleaned_app_df.groupby(["Category", "Type"], as_index=False).agg({'App': pandas.Series.count})
print(df_free_vs_paid.head())

g_bar = px.bar(df_free_vs_paid,
               x='Category',
               y='App',
               title='Free vs Paid Apps by Category',
               color='Type',
               barmode='group')
 
g_bar.update_layout(xaxis_title='Category',
                    yaxis_title='Number of Apps',
                    xaxis={'categoryorder':'total descending'},
                    yaxis=dict(type='log'))
 
g_bar.show()

box = px.box(cleaned_app_df,
             y='Installs',
             x='Type',
             color='Type',
             notched=True,
             points='all',
             title='How Many Downloads are Paid Apps Giving Up?')
 
box.update_layout(yaxis=dict(type='log'))
 
box.show()

df_paid_apps = cleaned_app_df[cleaned_app_df['Type'] == 'Paid']
box = px.box(df_paid_apps, 
             x='Category', 
             y='Revenue_Estimate',
             title='How Much Can Paid Apps Earn?')
 
box.update_layout(xaxis_title='Category',
                  yaxis_title='Paid App Ballpark Revenue',
                  xaxis={'categoryorder':'min ascending'},
                  yaxis=dict(type='log'))
 
 
box.show()

box = px.box(df_paid_apps,
             x='Category',
             y="Price",
             title='Price per Category')
 
box.update_layout(xaxis_title='Category',
                  yaxis_title='Paid App Price',
                  xaxis={'categoryorder':'max descending'},
                  yaxis=dict(type='log'))
 
box.show()
# %% 