
import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv("C:/Users/RSiu9/OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 73/QueryResults.csv", names=['DATE', 'TAG', 'POSTS'])
clean_df = df.dropna()
num_rows = clean_df.count()
languages = clean_df.groupby('TAG')
print(languages.sum())
print(languages.count())

clean_df['DATE'] = pandas.to_datetime(clean_df['DATE'])
print(clean_df)

reshaped_df = clean_df.pivot(index='DATE', columns='TAG', values='POSTS')
reshaped_df.fillna(0, inplace=True)
print(reshaped_df)
print(reshaped_df.shape)
print(reshaped_df.columns)
print(reshaped_df.isna().values.any())

# The window is number of observations that are averaged


#%%
roll_df = reshaped_df.rolling(window=3).mean()
plt.title('Java Posts On Stack Overflow')
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

for column in roll_df.columns:
    plt.plot(reshaped_df.index, roll_df[column], 
             linewidth=1, label=roll_df[column].name)

plt.legend(fontsize=8) 
#plt.plot(reshaped_df.index, reshaped_df['java'])
#plt.plot(reshaped_df.index, reshaped_df['python'])


# %%
