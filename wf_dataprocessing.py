import pandas as pd

def process():
    filename = "./data_original/Occupancy_Estimation.csv"
    read_dataset(filename)

def get_temp_value(df):
    # Averaging the temperature values received from four different sensors
    select_temp_cols = ['S1_Temp', 'S2_Temp', 'S3_Temp', 'S4_Temp']
    avg_temp = []
    for i in df.index:
        val = 0
        for col in select_temp_cols:
            val += df.loc[i, col]
        avg = val/len(select_temp_cols)
        avg_temp.append(avg)
    df['Temp_Avg'] = avg_temp

def read_dataset(filename):
    df = pd.read_csv(filename)
    get_temp_value(df)
    df.to_csv('./data_processed/Occupancy_Estimation_processed.csv')
