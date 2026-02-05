"""
Day 14 Activity: Full Cleaning Pipeline
Tasks:
1) Build clean_data() that orchestrates type, missing, outliers, strings/dates
2) Add basic validation checks
3) Run end-to-end and inspect
"""

import pandas as pd
import numpy as np

df = pd.read_csv('day14_users_raw.csv')
df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['income'] = pd.to_numeric(df['income'], errors='coerce')
df = df.dropna()
df = df[df['age'] > 0]
df = df[df['income'] < 1000000]
df['city'] = df['city'].str.strip()
df['signup_time'] = pd.to_datetime(df['signup_time'])
print(df.dtypes)
print(df.isnull().sum())
print(df)
