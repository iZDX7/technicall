import pandas as pd

df = pd.read_csv('D.csv')

print("Original dataset shape:", df.shape)

Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1

print("Q1 (25th percentile):", Q1)
print("Q3 (75th percentile):", Q3)
print("IQR (Interquartile Range):", IQR)

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("Lower bound for outliers:", lower_bound)
print("Upper bound for outliers:", upper_bound)

outliers = df[(df['Salary'] < lower_bound) | (df['Salary'] > upper_bound)]

print("Number of outliers:", len(outliers))
print("Outlier IDs and Salaries:")
for index, row in outliers.iterrows():
    print(f"ID: {row['ID']}, Salary: {row['Salary']}")

df_clean = df[(df['Salary'] >= lower_bound) & (df['Salary'] <= upper_bound)]

print("Cleaned dataset shape:", df_clean.shape)

df_clean.to_csv('D_clean.csv', index=False)
print("Cleaned dataset saved as D_clean.csv")