import pandas as pd
import numpy as np

# Reproducible results
np.random.seed(42)

# Number of transactions
N = 100_000

# -----------------------------
# Basic transaction information
# -----------------------------

order_ids = np.arange(1000001, 1000001 + N)

dates = pd.date_range(
    start="2025-01-01",
    end="2026-08-31",
    periods=N
)

customer_ids = np.random.randint(10001, 30001, N)

regions = np.random.choice(
    ["North", "South", "East", "West", "Central"],
    N
)

customer_segments = np.random.choice(
    ["Consumer", "Corporate", "Small Business"],
    N,
    p=[0.60, 0.25, 0.15]
)

channels = np.random.choice(
    ["Website", "Mobile App", "Marketplace"],
    N,
    p=[0.45, 0.35, 0.20]
)

# -----------------------------
# Product information
# -----------------------------

products = [
    "Laptop",
    "Smartphone",
    "Monitor",
    "Headphones",
    "Office Chair",
    "Shoes",
    "Books Bundle",
    "Skincare Kit",
    "Fitness Tracker"
]

categories = {
    "Laptop": "Electronics",
    "Smartphone": "Electronics",
    "Monitor": "Electronics",
    "Headphones": "Electronics",
    "Office Chair": "Home",
    "Shoes": "Fashion",
    "Books Bundle": "Books",
    "Skincare Kit": "Beauty",
    "Fitness Tracker": "Sports"
}

prices = {
    "Laptop": 810,
    "Smartphone": 585,
    "Monitor": 478.40,
    "Headphones": 171,
    "Office Chair": 266,
    "Shoes": 136,
    "Books Bundle": 171,
    "Skincare Kit": 145.20,
    "Fitness Tracker": 123.50
}

product = np.random.choice(products, N)

category = [categories[p] for p in product]

unit_price = np.array([prices[p] for p in product])

# -----------------------------
# Transaction metrics
# -----------------------------

quantity = np.random.randint(1, 5, N)

discount_pct = np.random.choice(
    [0, 5, 10, 15, 20],
    N,
    p=[0.20, 0.25, 0.30, 0.20, 0.05]
)

revenue = quantity * unit_price * (1 - discount_pct / 100)

# Approximate cost structure
cost_ratio = np.random.uniform(0.55, 0.80, N)

cost = revenue * cost_ratio

profit = revenue - cost

returned = np.random.choice(
    [0, 1],
    N,
    p=[0.92, 0.08]
)

satisfaction_score = np.round(
    np.clip(
        np.random.normal(4.1, 0.6, N),
        1,
        5
    ),
    1
)

delivery_days = np.round(
    np.random.uniform(1, 10, N),
    1
)

# -----------------------------
# Create DataFrame
# -----------------------------

df = pd.DataFrame({
    "order_id": order_ids,
    "order_date": dates,
    "customer_id": customer_ids,
    "region": regions,
    "customer_segment": customer_segments,
    "channel": channels,
    "category": category,
    "product": product,
    "quantity": quantity,
    "unit_price": np.round(unit_price, 2),
    "discount_pct": discount_pct,
    "revenue": np.round(revenue, 2),
    "cost": np.round(cost, 2),
    "profit": np.round(profit, 2),
    "returned": returned,
    "satisfaction_score": satisfaction_score,
    "delivery_days": delivery_days
})

# -----------------------------
# Save dataset
# -----------------------------

from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
output_file = PROJECT_DIR / "data" / "ecommerce_orders_large.csv"

output_file.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(output_file, index=False)

print("Dataset generated successfully!")
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")
print(f"Saved to: {output_file}")

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())