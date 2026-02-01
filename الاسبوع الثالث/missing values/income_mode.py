import pandas as pd
# data = {
#     "income_reported": [50000, 60000, None, 75000, None, 80000, 60000]
# }
data = pd.read_csv("deepseek_csv_20260201_5252ac.csv")
df_ind = data.copy()
for col in ["Age", "Salary"]:
    df_ind[col + "_missing"] = df_ind[col].isna().astype(int) 
    mean_val = df_ind[col].mean()
    med_val = df_ind[col].median()
    mode_val = df_ind[col].mode()[0]
    df_ind[col + "_mean_imp"] = df_ind[col].fillna(mean_val)
    df_ind[col + "_median_imp"] = df_ind[col].fillna(med_val)
    df_ind[col + "_mode_imp"] = df_ind[col].fillna(mode_val)
print(df_ind.head())