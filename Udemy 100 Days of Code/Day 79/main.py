import pandas as pd
import seaborn as sns
import plotly.express as px

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
