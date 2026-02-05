import pandas as pd


df = pd.read_csv('Lap3.csv')
cols = ['Age', 'Salary', 'Experience_Years']
for col in cols:
    df[col] = pd.to_numeric(df[col].astype(str).str.replace(r'[^\d.-]', '', regex=True), errors='coerce')
print(df.head())
print(df[cols].describe())
print(df.dtypes)