import pandas as pd

def aggregate_hourly_demand(df):
    df = df.copy()
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['pickup_hour'] = df['tpep_pickup_datetime'].dt.floor('h')

    demand_df = (
        df.groupby(['pickup_hour', 'PULocationID'])
        .size()
        .reset_index(name='demand')
    )

    return demand_df