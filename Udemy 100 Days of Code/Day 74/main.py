#%%
import pandas as pd
import matplotlib.pyplot as plt

sets_df = pd.read_csv('C:/Users/RSiu9/OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 74/static/data/sets.csv')
#print("first LEGO sets\n",sets_df.sort_values('year', ascending=True)['name'].head(),"\n")
#print("different lego products\n",sets_df[sets_df['year']==1949],"\n")
#print("top 5\n", sets_df.sort_values('num_parts', ascending=False).head())
# sets_by_year = sets_df.groupby('year').count()
# ax1 = plt.gca() #get current axis
# ax2 = ax1.twinx()

# ax1.title("LEGO Sets Sold by Year")
# ax1.set_xlabel('Year', fontsize=14)
# ax1.set_ylabel('Number of Sets', fontsize=14)
# ax1.plot(sets_by_year.index[:-2], sets_by_year.name[:-2])

# themes_by_year = sets_df.groupby('year').agg({'theme_id': pd.Series.nunique})
# themes_by_year.rename(columns={'theme_id':'nr_themes'}, inplace=True)
# #print(themes_by_year)

# #plt.title("Number of LEGO Themes by Year")
# #plt.xlabel('Year', fontsize=14)
# ax2.set_ylabel('Number of Themes', fontsize=14)
# ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], color='green')

parts_per_set = sets_df.groupby('year')['num_parts'].mean()
# alternative call:
# parts_per_set = sets_df.groupby('year').agg({'num_parts':pd.Series.mean})
pd.options.display.float_format = '{:,.1f}'.format
#plt.scatter(parts_per_set.index[:-2], parts_per_set[:-2])

set_theme_count = sets_df["theme_id"].value_counts()
#print(set_theme_count[:5])

theme_df = pd.read_csv('C:/Users/RSiu9/OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 74/static/data/themes.csv')
starwars_df = theme_df.groupby('name')

set_theme_count = pd.DataFrame({'id': set_theme_count.index, 
                               'set_count': set_theme_count.values})
#print(set_theme_count.head())

merged_df = pd.merge(set_theme_count, theme_df, on='id')
print(merged_df[:3])
plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Num of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
plt.bar(merged_df.name[:10], merged_df.set_count[:10])

#for x in set_theme_count[:5]:
#    print(x)
#print(sets_df[sets_df['theme_id']==158])

#%%

# from flask import Flask, render_template
# from flask_bootstrap import Bootstrap5

# app = Flask(__name__)
# Bootstrap5(app)

# @app.route('/')
# def home():
    
#     color_df = pd.read_csv('./Udemy 100 Days of Code/Day 74/static/data/colors.csv')
    
#     
    
   
#     # num_colors = color_df['rgb'].nunique()
#     # num_t = color_df.groupby('is_trans').count()
#     # colors = color_df.is_trans.value_counts()
#     # print(colors)
    
    

#     return render_template('index.html')



# if __name__ == "__main__":
#     app.run(debug=True)