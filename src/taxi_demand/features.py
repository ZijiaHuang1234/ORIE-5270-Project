def create_features(demand_df):
    df = demand_df.copy()

    df['hour'] = df['pickup_hour'].dt.hour
    df['day_of_week'] = df['pickup_hour'].dt.dayofweek
    df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)

    df = df.sort_values(['PULocationID', 'pickup_hour'])

    df['lag_1'] = df.groupby('PULocationID')['demand'].shift(1)
    df['lag_3_mean'] = (
        df.groupby('PULocationID')['demand']
        .shift(1)
        .rolling(3)
        .mean()
    )

    df['target'] = df.groupby('PULocationID')['demand'].shift(-1)

    return df.dropna()