import matplotlib.pyplot as plt
import pandas as pd

def visualize():
    filename = "./data_processed/Occupancy_Estimation_processed.csv"
    read_dataset(filename)

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

    #Calculating the frequency of each category
    num_cat = 2
    freq0 = 0
    freq1 = 0
    sensor_vals = list(df['S6_PIR'])
    for i in range(len(sensor_vals)):
        if sensor_vals[i]==0 :
            freq0 += 1
        else:
            freq1 += 1

    if(freq0>=freq1):
        most_freq = "0"
        less_freq = "1"
    else:
        most_freq = "1"
        less_freq = "0"

    # Writing everything to file
    with open("./data_processed/summary.txt","w+") as f:
        f.write("Quantitative features: \n")
        for i in range(4):
            f.write(selected_features[i]+"\n")
            f.write("Maximum: " + str(maximums[i])+"\n")
            f.write("Minimum: " + str(minimums[i])+"\n")
            f.write("Median: " + str(medians[i])+"\n")
            f.write("\n")
        f.write("Qualitative features: \n")
        f.write("Number of categories:" + str(num_cat) + "\n")
        f.write("Most frequent category: " + str(most_freq) + "\n")
        f.write("Least frequent category: " + str(less_freq) + "\n")

def calculate_corr_matrix(df):
    corr_columns = ['Temp_Avg', 'S1_Light', 'S1_Sound', 'S5_CO2']
    new_df = df[corr_columns]
    corr_matrix = new_df.corr()
    with open("./data_processed/correlations.txt","w+") as f:
        f.write(str(corr_matrix))

def scatter_plot(df):
    fig, ax = plt.subplots()
    fig.suptitle("Average Temperature vs Light")
    ax.set(xlabel = 'Temperature(in Celsius)', ylabel= 'Light(in Lux)')
    for i in df.index:
        x_vals = list(df['Temp_Avg'])
        y_vals = list(df['S1_Light'])
    plt.scatter(x_vals, y_vals, color='gray')
    plt.savefig("./visuals/TempVsLight.png")

    fig2, ax2 = plt.subplots()
    fig2.suptitle("Average Temperature vs Sound")
    ax2.set(xlabel = 'Temperature(in Celsius)', ylabel= 'Sound(in Volts)')
    for i in df.index:
        x_vals = list(df['Temp_Avg'])
        y_vals = list(df['S1_Sound'])
    plt.scatter(x_vals, y_vals, color='red')
    plt.savefig("./visuals/TempVsSound.png")

    fig3, ax3 = plt.subplots()
    fig3.suptitle("Average Temperature vs CO2 Concentration")
    ax3.set(xlabel = 'Temperature(in Celsius)', ylabel= 'CO2 Concentration(in ppm)')
    for i in df.index:
        x_vals = list(df['Temp_Avg'])
        y_vals = list(df['S5_CO2'])
    plt.scatter(x_vals, y_vals)
    plt.savefig("./visuals/TempVsCO2Conc.png")

    fig4, ax4 = plt.subplots()
    fig4.suptitle("Light vs Sound")
    ax4.set(xlabel = 'Light(in Lux)', ylabel= 'Sound(in Volts)')
    for i in df.index:
        x_vals = list(df['S1_Light'])
        y_vals = list(df['S1_Sound'])
    plt.scatter(x_vals, y_vals, color='orange')
    plt.savefig("./visuals/LightVsSound.png")

    fig5, ax5 = plt.subplots()
    fig5.suptitle("Light vs Co2Concentration")
    ax5.set(xlabel = 'Light(in Lux)', ylabel= 'CO2 Concentration(in ppm)')
    for i in df.index:
        x_vals = list(df['S1_Light'])
        y_vals = list(df['S5_CO2'])
    plt.scatter(x_vals, y_vals, color='pink')
    plt.savefig("./visuals/LightVsCo2Conc.png")

    fig6, ax6 = plt.subplots()
    fig6.suptitle("Sound vs Co2Concentration")
    ax6.set(xlabel = 'Sound(in Volts)', ylabel= 'CO2 Concentration(in ppm)')
    for i in df.index:
        x_vals = list(df['S1_Sound'])
        y_vals = list(df['S5_CO2'])
    plt.scatter(x_vals, y_vals, color='green')
    plt.savefig("./visuals/SoundVsCo2Conc.png")

def hist(df):
    sensor_vals = list(df['S6_PIR'])
    figure, axes= plt.subplots()
    figure.suptitle("The frequency of values in PIR sensor")
    axes.set(xlabel = 'Value', ylabel= 'Frequency')
    axes.hist(sensor_vals)
    plt.savefig("./visuals/PIRhistogram.png")

def read_dataset(filename):
    df = pd.read_csv(filename)
    compute_statistics(df)
    calculate_corr_matrix(df)
    scatter_plot(df)
    hist(df)
