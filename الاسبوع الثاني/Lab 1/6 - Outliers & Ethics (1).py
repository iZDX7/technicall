import pandas as pd 
df_out = pd.read_csv("day10_outliers.csv")

def iqr_bounds(s, k=1.5):
    Q1 = s.quantile(0.25)
    Q3 = s.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - k * IQR
    upper_bound = Q3 + k * IQR
    return lower_bound, upper_bound

lower, upper = iqr_bounds(df_out["income"], k=1.5)
print("Lower Bound:", lower)
print("Upper Bound:", upper)
mask_iqr = (df_out["income"] < lower) | (df_out["income"] > upper)

print("\noutliers:")
print(df_out[mask_iqr])
print("\nNon-outliers:")
print(df_out[~mask_iqr])  