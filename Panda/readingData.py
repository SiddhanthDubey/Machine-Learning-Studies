import pandas as pd

df = pd.read_csv('pokemon_data.csv')

print(df.columns)

# Read each column
print(df['Name'])
print((df['Name'].head(4)))

print(df[['Name','HP','Legendary']])
print(df.iloc[2,1])
print(df.loc[df['Type 1'] == "Fire"])

print(df.describe())
print(df.sort_values('Name',ascending=False))
print(df.sort_values(['Type 1','HP']))
print(df.sort_values(['Type 1','HP'],ascending=[1,0]))