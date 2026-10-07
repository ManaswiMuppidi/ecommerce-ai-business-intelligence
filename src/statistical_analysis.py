import pandas as pd
from scipy.stats import pearsonr

df=pd.read_csv("data/ecommerce_orders_large.csv")
r,p=pearsonr(df["delivery_days"],df["satisfaction_score"])
print(f"Correlation between delivery time and satisfaction: r={r:.3f}, p={p:.4f}")
