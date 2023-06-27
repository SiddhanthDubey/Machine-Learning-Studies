import pandas as pd
df = pd.read_csv('pokemon_data.csv')

df['Total'] = df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed']

df.to_csv('modified.csv')

print(pd.read_csv('modified.csv'))