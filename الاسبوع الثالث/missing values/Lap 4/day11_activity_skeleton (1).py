import pandas as pd
import numpy as np

df = pd.read_csv('day11_income.csv')

def winsorize_series(s, lower_q, upper_q):
    lower_bound = s.quantile(lower_q)
    upper_bound = s.quantile(upper_q)
    return s.clip(lower=lower_bound, upper=upper_bound)

def remove_upper_tail(s, upper_q):
    upper_bound = s.quantile(upper_q)
    return s[s <= upper_bound]

print("Original:")
print(df.describe())
winsorized = winsorize_series(df['income'], 0.05, 0.95)
print("Winsorized:")
print(winsorized.describe())
removed = remove_upper_tail(df['income'], 0.95)
print("Removed upper tail:")
print(removed.describe())
