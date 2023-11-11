import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor

def create_model(df):
    X = df.drop(['Date', 'Time', 'Room_Occupancy_Count','S1_Temp','S2_Temp','S3_Temp','S4_Temp'], axis=1)
    Y = df['Room_Occupancy_Count']

    rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_regressor.fit(X, Y)
    with open("models/random_forest_model.pickle", 'wb') as file:
        pickle.dump(rf_regressor, file)
