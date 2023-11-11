import pandas as pd
from wf_ml_training import create_model
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

def create_train_test_set():
    df = pd.read_csv("data_processed/Occupancy_Estimation_processed.csv")
    df = shuffle(df)
    train_dataset, test_dataset = train_test_split(df, test_size=0.2)
    train_dataset.to_csv("data_processed/train.csv")
    test_dataset.to_csv("data_processed/test.csv")
    return train_dataset

def train():
    data = create_train_test_set()
    create_model(data)
    
train()

