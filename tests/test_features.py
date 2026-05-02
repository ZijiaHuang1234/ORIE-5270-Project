import pandas as pd
from taxi_demand.features import create_features

def test_feature_columns():
    data = {
        'pickup_hour': pd.date_range(start='2026-01-01', periods=5, freq='h'),
        'PULocationID': [1]*5,
        'demand': [10, 20, 30, 40, 50]
    }

    df = pd.DataFrame(data)
    result = create_features(df)

    assert 'lag_1' in result.columns
    assert 'target' in result.columns