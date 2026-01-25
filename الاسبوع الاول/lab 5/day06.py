import pandas as pd

df = pd.read_csv('day06_user_data.csv')

df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['income'] = pd.to_numeric(df['income'], errors='coerce')

df['age'].fillna(df['age'].mean(), inplace=True)
df['income'].fillna(df['income'].mean(), inplace=True)
df['city'].fillna('Unknown', inplace=True)

print(df)
