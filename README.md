# NYC Taxi Demand Prediction

## Project Overview

This project builds a machine learning pipeline to predict next-hour demand for NYC yellow taxis using real-world trip record data. The system processes raw trip-level data, aggregates it into hourly demand by pickup location, constructs time-based and lag-based features, and trains a regression model to forecast future demand.

The project is designed as a reproducible Python package with modular components and unit tests.


## Dataset

The project uses NYC Yellow Taxi Trip Record data for:

* December 2025
* January 2026
* February 2026

Data source: NYC Taxi and Limousine Commission (TLC)

The raw data is stored locally in:

```
Data_YellowTaxiRecord_3mo/
```

Each file is in parquet format and contains trip-level information such as pickup time and location.


## Problem Definition

The goal is to predict the number of taxi trips (demand) for the next hour at a given pickup location.

* Input: historical demand and time-based features
* Output: next-hour demand

This is a time-series regression problem.


## Methodology

The pipeline consists of the following steps:

### 1. Data Aggregation

Trip-level records are aggregated into hourly demand grouped by `PULocationID`.

### 2. Feature Engineering

The following features are created:

**Time-based features**

* hour
* day_of_week
* is_weekend

**Lag-based features**

* lag_1 (previous hour demand)
* lag_3_mean (rolling average of previous 3 hours)

### 3. Model

A Random Forest Regressor is used to predict next-hour demand.

### 4. Evaluation

Model performance is evaluated using Root Mean Squared Error (RMSE).


## Project Structure

5270_Final_Project/
├── Data_YellowTaxiRecord_3mo/
│   ├── yellow_tripdata_2025-12.parquet
│   ├── yellow_tripdata_2026-01.parquet
│   ├── yellow_tripdata_2026-02.parquet
├── scripts/
│   └── run_pipeline.py
├── src/
│   └── taxi_demand/
│       ├── __init__.py
│       ├── aggregation.py
│       ├── features.py
│       ├── model.py
├── tests/
│   ├── conftest.py
│   ├── test_aggregation.py
│   ├── test_features.py
├── pytest.ini
├── requirements.txt
└── README.md


## Installation

Install required dependencies:


pip install pandas scikit-learn pyarrow pytest


## How to Run

Run the full pipeline from the project root directory:

python scripts/run_pipeline.py


## Testing

Run unit tests:

pytest

The tests validate:

* Hourly demand aggregation
* Feature engineering correctness


## Results

Baseline performance (naive lag-based prediction):

RMSE: 32.04

Model performance (Random Forest):

RMSE: 22.32

The Random Forest model substantially outperforms the baseline. The baseline uses the previous hour's demand (`lag_1`) as the prediction for the next hour, while the model incorporates additional temporal and lag-based features. This improvement suggests that the engineered features provide meaningful predictive value beyond a simple persistence assumption.


## Conclusion

This project demonstrates a complete end-to-end machine learning workflow for time-series demand prediction, including data processing, feature engineering, model training, and evaluation.

The modular package structure and unit tests ensure reproducibility and maintainability.


## Future Work

* Incorporate more historical data
* Add spatial features (neighboring locations)
* Try more advanced models (e.g., XGBoost, LSTM)
