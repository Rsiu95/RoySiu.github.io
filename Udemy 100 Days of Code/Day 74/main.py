#%%
import pandas as pd
import matplotlib.pyplot as plt
#from flask import Flask, render_template
#from flask_bootstrap import Bootstrap5



sets_df = pd.read_csv('C:/Users/RSiu9/OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 74/static/data/sets.csv')
#print("first LEGO sets\n",sets_df.sort_values('year', ascending=True)['name'].head(),"\n")
#print("different lego products\n",sets_df[sets_df['year']==1949],"\n")
#print("top 5\n", sets_df.sort_values('num_parts', ascending=False).head())
sets_by_year = sets_df.groupby('year').count()
print(sets_by_year)
plt.title("Number of LEGO Sets Sold by Year")
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Sets', fontsize=14)
plt.plot(sets_by_year.index[:-2], sets_by_year.name[:-2])
#%%


app = Flask(__name__)
Bootstrap5(app)

@app.route('/')
def home():
    
    color_df = pd.read_csv('./Udemy 100 Days of Code/Day 74/static/data/colors.csv')
    
    theme_df = pd.read_csv('./Udemy 100 Days of Code/Day 74/static/data/themes.csv')
    
   
    # num_colors = color_df['rgb'].nunique()
    # num_t = color_df.groupby('is_trans').count()
    # colors = color_df.is_trans.value_counts()
    # print(colors)
    
    

    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)