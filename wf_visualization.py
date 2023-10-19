import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def visualize():
    print("Data visualize")

def compute_statistics(df):
    # Qualitative: S6_PIR, has either 0 or 1 value
    # Rest are quantitative
    selected_features = ['Temp_Avg', 'S1_Light', 'S1_Sound', 'S5_CO2', 'S6_PIR']
    # List of max, min and median of quantative feature in order. 
    maximums = []
    minimums = []
    medians = []
    new_df = df[selected_features]
    for feature in selected_features:
        maximums.append(max(new_df[feature]))
        minimums.append(min(new_df[feature]))
        values = list(new_df[feature])
        values.sort()
        mid = len(values) // 2
        res = (values[mid]+values[~mid])/2
        medians.append(res)
    # Removing last feature from the lists since it is not quantitative
    maximums.pop()
    minimums.pop()
    medians.pop()
    with open("./data_processed/summary.txt","w+") as f:
        for i in range(4):
            f.write(selected_features[i]+"\n")
            f.write("Maximum: " + str(maximums[i])+"\n")
            f.write("Minimum: " + str(minimums[i])+"\n")
            f.write("Median: " + str(medians[i])+"\n")
            f.write("\n")

def calculate_corr_matrix(df):
    corr_columns = ['Temp_Avg', 'S1_Light', 'S1_Sound', 'S5_CO2']
    new_df = df[corr_columns]
    corr_matrix = new_df.corr()
    with open("./data_processed/correlations.txt","w+") as f:
        f.write(str(corr_matrix))


def read_dataset(filename):
    df = pd.read_csv(filename)
    compute_statistics(df)
    calculate_corr_matrix(df)

if __name__ == '__main__':
    filename = "./data_processed/Occupancy_Estimation_processed.csv"
    read_dataset(filename)