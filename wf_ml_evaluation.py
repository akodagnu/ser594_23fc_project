import pandas as pd
from wf_ml_training import create_model
from wf_ml_prediction import predict
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

def create_train_test_set():
    df = pd.read_csv("data_processed/Occupancy_Estimation_processed.csv")
    df = shuffle(df)
    train_dataset, test_dataset = train_test_split(df, test_size=0.2)
    train_dataset.to_csv("data_processed/train.csv", index=False)
    test_dataset.to_csv("data_processed/test.csv", index=False)
    return train_dataset

def train():
    print("Creating train and test dataset")
    data = create_train_test_set()
    print("Creating model")
    create_model(data)
    print("Predicting output")
    mse, r2_score = predict()
    print("Writing metrics to summary file")
    with open("evaluation/summary.txt","w+") as f:
        f.write("Dataset \t\t\t\t\t\t\t Mean Squared Error \t\t\t R2 score \n")
        f.write("Occupancy_Estimation_processed.csv" + "\t" + str(mse) + "\t\t\t" + str(r2_score))
    
train()

