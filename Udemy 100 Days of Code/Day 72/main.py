import pandas

df = pandas.read_csv('./Udemy 100 Days of Code/Day 72/salaries_by_college_major.csv')

# view top 5 rows of file
print("Top 5 Rows\n", df.head(), "\n")

# view number of rows and columns
print("Number of Rows and Columns\n", df.shape, "\n")

# access columns directly
print("Print columns directly\n", df.columns, "\n")

# view NaN or blank cells in csv
print("View NaN/blank cells\n", df.isna, "\n")

# print last 5 rows of file
print("View last 5 rows\n", df.tail(), "\n")

# remove NaN/blank cells
clean_df = df.dropna()
cleaned_data = clean_df.tail()
print("NaN/blank cells removed\n", cleaned_data, "\n")

# Accessing a particular column
print(clean_df['Starting Median Salary'], "\n")

# Find index of max value based on column
print(clean_df["Starting Median Salary"].idxmax(), "\n")

# view corresponding column based on index
print(clean_df['Undergraduate Major'].loc[43], "\n")

# viewing data corresponding to index
print(clean_df.loc[43], "\n")

# Challenge
print(clean_df.loc[clean_df['Mid-Career Median Salary'].idxmax()])

print(clean_df.loc[clean_df['Starting Median Salary'].idxmin()])

print(clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()])

# Calculate he difference between the earnings of the 10th and 90th percentile
print(clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary'])
# Or use .subtract() method.
print(clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary']))

# add output of above into its own pandas dataframe column with .insert()
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
#syntax: .insert([column],'title', [data])
clean_df.insert(1, 'Spread', spread_col)
print(clean_df.head())

# sorting by lowest spread
low_risk = clean_df.sort_values('Spread')
print(low_risk[['Undergraduate Major', 'Spread']].head())

# Challenge
print(clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)['Undergraduate Major'].head())
print(clean_df.sort_values('Spread', ascending=False)['Undergraduate Major'].head())
print(clean_df.sort_values('Mid-Career Median Salary', ascending=False)['Undergraduate Major'].head())

# grouping based in column
print(clean_df.groupby('Group').count())

# find mean 
print(clean_df.groupby('Group').mean())

# to format 2 decimals
pandas.options.display.float_format = '{:,.2f}'.format