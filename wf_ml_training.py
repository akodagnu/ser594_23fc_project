import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def create_model(df):
    X = df.drop(['Date', 'Time', 'Room_Occupancy_Count','S1_Temp','S2_Temp','S3_Temp','S4_Temp'], axis=1)
    Y = df['Room_Occupancy_Count']

    rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_regressor.fit(X, Y)

    # Model 2 : Using hyperparamter tuning (n_estimators, max_depth) to see if I get better results.
    rf_regressor_2 = RandomForestRegressor(random_state=42, n_estimators=50, max_depth=20)
    rf_regressor_2.fit(X,Y)

    # Model 3 : Using hyperparamter tuning (max_features) to see if I get better results.
    rf_regressor_3 = RandomForestRegressor(random_state=42, max_features=2)
    rf_regressor_3.fit(X,Y)

    # Model 4 and 5: Splitting my training data into two subsets
    data_subset1, data_subset2 = train_test_split(df, test_size=0.3)
    X1 = data_subset1.drop(['Date', 'Time', 'Room_Occupancy_Count','S1_Temp','S2_Temp','S3_Temp','S4_Temp'], axis=1)
    Y1 = data_subset1['Room_Occupancy_Count']
    rf_regressor_4 = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_regressor_4.fit(X1, Y1)

    X2 = data_subset2.drop(['Date', 'Time', 'Room_Occupancy_Count','S1_Temp','S2_Temp','S3_Temp','S4_Temp'], axis=1)
    Y2 = data_subset2['Room_Occupancy_Count']
    rf_regressor_5 = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_regressor_5.fit(X2, Y2)

    # Storing models
    with open("models/random_forest_model1.pickle", 'wb') as file:
        pickle.dump(rf_regressor, file)

    with open("models/random_forest_model2.pickle", 'wb') as file:
        pickle.dump(rf_regressor_2, file)

    with open("models/random_forest_model3.pickle", 'wb') as file:
        pickle.dump(rf_regressor_3, file)

    with open("models/random_forest_model4.pickle", 'wb') as file:
        pickle.dump(rf_regressor_4, file)

    with open("models/random_forest_model5.pickle", 'wb') as file:
        pickle.dump(rf_regressor_5, file)

def create_new_model(df):
    X = df[['S5_CO2']]
    Y = df['Room_Occupancy_Count']

    rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_regressor.fit(X, Y)
    with open("models/random_forest_model_CO2.pickle", 'wb') as file:
        pickle.dump(rf_regressor, file)