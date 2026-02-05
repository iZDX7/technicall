import pandas as pd
df = pd.read_csv("dataset.csv").drop_duplicates()
df.columns = df.columns.str.strip().str.lower()
df["city"] = df["city"].str.strip().str.title()
df["country"] = df["country"].str.strip().str.title()
df["registration_date"] = pd.to_datetime(df["registration_date"], errors="coerce", dayfirst=True)
df["last_login_date"] = pd.to_datetime(df["last_login_date"], errors="coerce")
df["order_date_time"] = pd.to_datetime(df["order_date_time"], errors="coerce")
df.loc[(df["age"] < 13) | (df["age"] > 100), "age"] = pd.NA
df.loc[df["salary"] < 0, "salary"] = pd.NA
df.loc[df["quantity"] <= 0, "quantity"] = pd.NA
df.loc[df["total_amount"] <= 0, "total_amount"] = pd.NA
df.loc[(df["discount_percent"] < 0) | (df["discount_percent"] > 100), "discount_percent"] = pd.NA
df.loc[(df["customer_score"] < 0) | (df["customer_score"] > 100), "customer_score"] = pd.NA
df.loc[df["transaction_count"] < 0, "transaction_count"] = pd.NA
num = df.select_dtypes("number").columns
obj = df.select_dtypes("object").columns
df[num] = df[num].fillna(df[num].median())
df[obj] = df[obj].apply(lambda x: x.fillna(x.mode()[0]))
city_sales = df.groupby("city")["total_amount"].sum().reset_index()
top_categories = df.groupby("product_category")["quantity"].sum().reset_index()
df.to_csv("cleaned_dataset.csv", index=False)