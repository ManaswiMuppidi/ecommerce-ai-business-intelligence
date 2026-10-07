import pandas as pd

df = pd.read_csv("data/ecommerce_orders_large.csv")
print("Shape:", df.shape)
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicate order IDs:", df.order_id.duplicated().sum())
print("\nNegative revenue:", (df.revenue < 0).sum())
print("\nSummary:\n", df.describe())
