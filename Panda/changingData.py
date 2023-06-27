import pandas as pd


df = pd.read_csv('pokemon_data.csv')
print(df)

df['Total'] = df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed']
print(df)

df = df.drop(columns=['Total'])
print(df)
df_2_0 = df
df = df.drop(columns=['Name','Legendary'])
print(df)
df = df_2_0
print(df)

df['Total'] = list(df.iloc[:,4:10].sum(axis=1))
print(df)

# To change the position of columns

cols = df.columns.values
df = df[cols[0:4]+[cols[-1]]+cols[4:13]]
