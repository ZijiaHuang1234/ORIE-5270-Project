import pandas as pd
from taxi_demand.model import train_model

def test_train_model_runs():
    X = pd.DataFrame({
        "lag_1": [10, 20, 30],
        "lag_3_mean": [10, 20, 30],
        "hour": [1, 2, 3],
        "day_of_week": [1, 2, 3],
        "is_weekend": [0, 0, 1]
    })

    y = [20, 30, 40]

    model = train_model(X, y)

    preds = model.predict(X)

    assert len(preds) == len(X)