import pandas as pd
import pickle
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

def predict(filename):
    with open(filename, 'rb') as file:
        loaded_model = pickle.load(file)
    test_data = pd.read_csv("data_processed/test.csv")
    # Dropping the same columns as my train data
    X_Test = test_data.drop(['Date', 'Time', 'Room_Occupancy_Count','S1_Temp','S2_Temp','S3_Temp','S4_Temp'], axis=1)
    Y_Test = test_data['Room_Occupancy_Count']

    Y_Pred = loaded_model.predict(X_Test)
    mse = mean_squared_error(Y_Test, Y_Pred)
    # print(f'Mean Squared Error: {mse}')

    Y_Pred_Test = loaded_model.predict(X_Test)

    # Calculate R-squared for test set
    r2_score_predict = r2_score(Y_Test, Y_Pred_Test)
    #print(f'R-squared (Test): {r2_test}')

    return mse, r2_score_predict
