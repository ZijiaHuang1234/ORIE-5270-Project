import pandas as pd
from taxi_demand.aggregation import aggregate_hourly_demand

def test_aggregation_basic():
    data = {
        'tpep_pickup_datetime': ['2026-01-01 10:10:00', '2026-01-01 10:20:00'],
        'PULocationID': [1, 1]
    }

    df = pd.DataFrame(data)
    result = aggregate_hourly_demand(df)

    assert result.iloc[0]['demand'] == 2
    