import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# Load the large synthetic dataset
df = pd.read_csv("data/ecommerce_orders_large.csv")


# Features and target
features = [
    "quantity",
    "unit_price",
    "discount_pct",
    "region",
    "channel",
    "category",
    "customer_segment",
    "returned",
    "satisfaction_score",
    "delivery_days"
]

target = "profit"

X = df[features]
y = df[target]


# Identify numerical and categorical columns
numerical_features = [
    "quantity",
    "unit_price",
    "discount_pct",
    "returned",
    "satisfaction_score",
    "delivery_days"
]

categorical_features = [
    "region",
    "channel",
    "category",
    "customer_segment"
]


# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("num", "passthrough", numerical_features),
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ]
)


# Random Forest model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)


# Complete ML pipeline
pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# Train
pipeline.fit(X_train, y_train)


# Predict
predictions = pipeline.predict(X_test)


# Evaluation
mae = mean_absolute_error(y_test, predictions)
rmse = mean_squared_error(y_test, predictions) ** 0.5
r2 = r2_score(y_test, predictions)


print("Random Forest Regression Results")
print("---------------------------------")
print(f"MAE:  {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R2:   {r2:.3f}")