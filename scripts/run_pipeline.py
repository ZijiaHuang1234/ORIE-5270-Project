import sys
from pathlib import Path
import math

import pandas as pd
from sklearn.metrics import mean_squared_error

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from taxi_demand.aggregation import aggregate_hourly_demand
from taxi_demand.features import create_features
from taxi_demand.model import train_model


df1 = pd.read_parquet(ROOT / "Data_YellowTaxiRecord_3mo" / "yellow_tripdata_2025-12.parquet")
df2 = pd.read_parquet(ROOT / "Data_YellowTaxiRecord_3mo" / "yellow_tripdata_2026-01.parquet")
df3 = pd.read_parquet(ROOT / "Data_YellowTaxiRecord_3mo" / "yellow_tripdata_2026-02.parquet")

df = pd.concat([df1, df2, df3], ignore_index=True)

demand_df = aggregate_hourly_demand(df)
feature_df = create_features(demand_df)

split_time = feature_df["pickup_hour"].quantile(0.8)

train = feature_df[feature_df["pickup_hour"] <= split_time]
test = feature_df[feature_df["pickup_hour"] > split_time]

feature_cols = ["lag_1", "lag_3_mean", "hour", "day_of_week", "is_weekend"]

X_train = train[feature_cols]
y_train = train["target"]

X_test = test[feature_cols]
y_test = test["target"]

model = train_model(X_train, y_train)
y_pred = model.predict(X_test)

# Baseline prediction: use previous hour demand
baseline_pred = X_test["lag_1"]
baseline_mse = mean_squared_error(y_test, baseline_pred)
baseline_rmse = math.sqrt(baseline_mse)

mse = mean_squared_error(y_test, y_pred)
rmse = math.sqrt(mse)

print("Baseline RMSE:", baseline_rmse)
print("Model RMSE:", rmse)