import pandas as pd

df = pd.read_csv("day08_events.csv")

df = df.drop_duplicates()
df = df.drop_duplicates(subset=["user", "day", "product"])
result = df.groupby("user").agg(
    event_count=("product", "count"),
    ever_clicked=("clicked", "max")
)

print(result)
