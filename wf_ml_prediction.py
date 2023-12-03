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
    # For experimentation and analysis, I am storing the predicted value
    # pred = pd.DataFrame(Y_Pred);
    # pred.to_csv("predicted_vals.csv")
    mse = mean_squared_error(Y_Test, Y_Pred)
    # print(f'Mean Squared Error: {mse}')

    Y_Pred_Test = loaded_model.predict(X_Test)

    # Calculate R-squared for test set
    r2_score_predict = r2_score(Y_Test, Y_Pred_Test)
    #print(f'R-squared (Test): {r2_test}')

    return mse, r2_score_predict

def predict_new(filename):
    with open(filename, 'rb') as file:
        loaded_model = pickle.load(file)
    test_data = pd.read_csv("data_original/co2_concentration.csv")
    # Dropping the same columns as my train data
    X_Test = test_data[['S5_CO2']]

    Y_Pred = loaded_model.predict(X_Test)
    with open("evaluation/prediction_data.txt","a+") as f:
        f.write(str(Y_Pred))