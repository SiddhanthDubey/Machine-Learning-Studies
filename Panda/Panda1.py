import pandas as pd

df = pd.read_csv('pokemon_data.csv')

print(df)

print(df.head(3))

print(df.tail(3))

df_xlsx = pd.read_excel('pokemon_data.xlsx')

print(df_xlsx)

df_text = pd.read_csv('pokemon_data.txt',delimiter='\t')