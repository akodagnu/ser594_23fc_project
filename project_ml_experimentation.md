#### SER594: Experimentation
#### Room Occupancy Estimation
#### Akshata Bharadwaj Kodagnur
#### 11/20/2023


## Explainable Records
### Record 1
**Raw Data:** 

| Time      | S1_Temp | S2_Temp | S3_Temp | S4_Temp | S1_Light | S2_Light | S3_Light | S4_Light | S1_Sound | S2_Sound | S3_Sound | S4_Sound | S5_CO2 | S5_CO2_Slope | S6_PIR | S7_PIR | Room_Occupancy_Count | Temp_Avg |
|-----------|---------|---------|---------|---------|----------|----------|----------|----------|----------|----------|----------|----------|--------|--------------|--------|--------|-----------------------|----------|
| 17:53:52  | 26      | 26.19   | 25.75   | 25.94   | 142      | 227      | 5        | 6        | 0.75     | 0.43     | 0.2      | 0.2      | 840    | -0.673076923 | 1      | 1      | 2                     | 25.97    |


**Prediction Explanation:** 
Predicted value of Room occupancy by my model = 2.
This is a reasonable prediction because the carbon dioxide concentration is high with a value of 840ppm and both the PIR sensors have detected movement in the room (denoted by 1). The sound values are also comparatively higher.

### Record 2
**Raw Data:** 

| Time     | S1_Temp | S2_Temp | S3_Temp | S4_Temp | S1_Light | S2_Light | S3_Light | S4_Light | S1_Sound | S2_Sound | S3_Sound | S4_Sound | S5_CO2 | S5_CO2_Slope | S6_PIR | S7_PIR | Room_Occupancy_Count | Temp_Avg |
|----------|---------|---------|---------|---------|----------|----------|----------|----------|----------|----------|----------|----------|--------|--------------|--------|--------|----------------------|----------|
| 8:50:55  | 25.13   | 25.13   | 24.63   | 25.38   | 6        | 7        | 35       | 22       | 0.07     | 0.05     | 0.06     | 0.07     | 360    | -0.030769231 | 0      | 0      | 0                    | 25.0675  |


**Prediction Explanation:** 
Predicted value of Room occupancy by my model = 0.
This is a reasonable prediction as well. The carbon dioxide level is pretty low compared the the first record, with a value of 360ppm. The sound values are very low and the PIR sensors have not detected any motion.

## Interesting Features
### Feature A
**Feature:** CO2 Concentration

**Justification:** Since we are trying to estimate the number of people that should occupy a room, carbon dioxide concentration plays a key role.
Since humans breathe in oxygen and give out carbon dioxide, higher carbon dioxide levels indicate there are more people in the room.

### Feature B
**Feature:** Temperature

**Justification:** Similar to carbon dioxide concentration, temperature is also proportional to the number of people in a room. The more the people in a room, the hotter it is. Carbon dioxide also leads to a rise in the temperature since it is a greenhouse gas.

## Experiments 
### Varying CO2 Concentration
**Prediction Trend Seen:** Keeping all the values of other columns the same, I varied only CO2 concentration. There is difference in the predicted values which show that CO2 concentration is a major factor. When the CO2 concetration is higher, the output is higher. But the value of mean squared error is also much higher than the original values.

### Varying Sound sensor values
**Prediction Trend Seen:** This time I varied the values obtained from the four sound sensors. For the rest of the columns, I maintained the same values. I did notice a change in the predicted values, but it was not as significant as the change I observed for CO2 concentration. When the sound values were higher, the output is higher too indicating there are more people in the room.

### Varying CO2 concentration and Sound sensor values together
**Prediction Trend Seen:** The predicted values definitely changed with the changing CO2 concentration and sound levels. When CO2 concentration and sound levels were high, the output was high. Also, the mean squeared error was lesser compared to the ones I got with varying just one of these two features.

### Varying CO2 concentration and Sound sensor values and B inversely
**Prediction Trend Seen:** There was a change in predicted values, but the mean squared error was high. I observed that the output followed the change in CO2 concentration rather than the sound level. Thus we can probably say that CO2 concentration is a more significant feature.
