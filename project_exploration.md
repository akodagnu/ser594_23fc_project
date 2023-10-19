#### SER594: Exploratory Data Munging and Visualization
#### Room Occupancy Estimation
#### Akshata Bharadwaj Kodagnur
#### 10/16/2023

## Basic Questions
**Dataset Author(s):** Adarsh Pal Singh, Sachin Chaudhari

**Dataset Construction Date:**  8/15/2023

**Dataset Record Count:** 10129

**Dataset Field Meanings:** First two fields are date and time. The rest of the fields are data from sensors. 
There are sensors for temperature, light, sound, carbon dioxide, infrared sensors for motion detection and the last field is for room occupancy count which is the target.

**Dataset File Hash(es):**  
URL: http://archive.ics.uci.edu/dataset/864/room+occupancy+estimation

md5 hash: f07c72f4d375929c27b141743c41fd46

## Interpretable Records
### Record 1
**Raw Data:** 

| Time     | S1_Temp | S2_Temp | S3_Temp | S4_Temp | S1_Light | S2_Light | S3_Light | S4_Light | S1_Sound | S2_Sound | S3_Sound | S4_Sound | S5_CO2 | S5_CO2_Slope | S6_PIR | S7_PIR | Room_Occupancy_Count |
|----------|---------|---------|---------|---------|----------|----------|----------|----------|----------|----------|----------|----------|-------|--------------|-------|-------|-----------------------|
| 10:52:45 | 25      | 24.75   | 24.56   | 25.44   | 120      | 34       | 54       | 40       | 1.39     | 0.32     | 0.43     | 0.06     | 390   | 0.076923077 | 1     | 0     | 1                     |


**Interpretation:**  
At 10:52am, the four sensors recorded temperatures of around 25 degrees celsius. The four light sensors record different values (in terms of Lux) since the test lab contained windows at certain areas of the room. 
Thus the sensors closer to windows might record a higher value. The next four columns correspond to the values from the sound sensors. The setup has self closing doors, variation in sound values might occur depending on the distance to the door and closing/opening of the door.
The concentration of CO2 recorded was 390ppm. The column 'Slope of CO2' was only added to boost performance of the model, does not hold a real life interpretation. The next sensor is a PIR sensor which detects motion. The columns contain binary values for each row, where the value is 0 if motion is not detected.
In this case, one of the sensors picked up some movement, but the other did not. Hence the values are 0 and 1 respectively.
The last column is the actual room occupancy count at that moment in time, this is the value that we hope to estimate correctly in the future.


### Record 2
**Raw Data:** 

| Time     | S1_Temp | S2_Temp | S3_Temp | S4_Temp | S1_Light | S2_Light | S3_Light | S4_Light | S1_Sound | S2_Sound | S3_Sound | S4_Sound | S5_CO2 | S5_CO2_Slope | S6_PIR | S7_PIR | Room_Occupancy_Count |
|----------|---------|---------|---------|---------|----------|----------|----------|----------|----------|----------|----------|----------|-------|--------------|-------|-------|-----------------------|
| 17:37:01 | 25.94   | 26.19   | 25.88   | 25.94   | 144      | 229      | 170      | 19       | 0.39     | 0.53     | 1.57     | 0.22     | 830   | 0.688461538 | 1     | 1     | 3                     |


**Interpretation:** 

At 5:37pm, the four temperature sensors record a temperature of around 26 degrees celsius. The four light sensors record 144, 229, 170 and 19 Lux respectively. 
The four sound sensors record 0.39, 0.53, 1.57 and 0.22 V respectively. The carbon dioxide concetration is currently 830ppm. Both the motion sensors have detected motion since the room is currently occupied by 3 people.
It is important to note that the concentration of CO2 detected is significantly larger in this case compared to our previous record. Since there are more people in the room, the concentration is justifiably higer.

## Background Domain Knowledge
A significant issue in the field of building energy management is a substantial portion of energy is consumed by heating, ventilation, and air conditioning (HVAC) systems. 
To enhance energy efficiency, the project focuses on making these systems demand-driven based on real-time human occupancy information. 
The main objective of this project is to estimate room occupancy using non-invasive methods i.e, data from sensors. 
Invasive measures like camera, RFIDs and wearables can violate data privacy and security if used incorrectly. Accurate room occupancy estimation can help us come up with intelligent ventilation systems and
air conditioners. 

The approach taken leverages a network of heterogeneous sensor nodes, including low-cost and non-intrusive sensors that measure parameters such as CO2 levels, temperature, illumination, sound, and motion. 
These sensors were strategically deployed in a room, arranged in a star configuration, and data was collected over a four-day period. 

The CO2 data appeared to give a great indicator for the number of inhabitants in the room after examining the time series plots of the sensors. However, it took a while for the values to stabilize when they started to climb or fall. 
As a result, the slope of CO2 was determined as a new characteristic.

Various supervised machine learning algorithms, such as linear discriminant analysis (LDA), quadratic discriminant analysis (QDA), support vector machine (SVM), and random forest (RF), were applied to different combinations of sensor data to estimate occupancy. 
Performance was evaluated using metrics like accuracy, F1 score, and confusion matrix. The results demonstrated a maximum accuracy of 98.4% and a high F1 score of 0.953 for estimating the number of occupants, showcasing the effectiveness of the approach.

**References:** 
1. https://ieeexplore-ieee-org.ezproxy1.lib.asu.edu/document/8644432
2. https://ieeexplore.ieee.org/abstract/document/7457116
3. https://dl-acm-org.ezproxy1.lib.asu.edu/doi/10.5555/2048536.2048555
4. https://www-sciencedirect-com.ezproxy1.lib.asu.edu/science/article/pii/S0378778815304357

Note: Some of the links require logging in with ASU credentials, especially to view the IEEE papers in the references.

## Data Transformation
### Transformation 1
**Description:** Getting an averaged temperature value

**Soundness Justification:** Most of the values in my dataset are already in a useful format. But, the temperature values obtained from the four different sensors can be averaged to get one temperature value.
This transformation mkaes sense only for temperature values since the values are similar, for the rest of the sensors, the values detected depends on various other factors like closeness to the doors and windows.

(duplicate above as many times as needed; remove this line when done)


## Visualization
### Visual N
**Analysis:** TODO

(duplicate above as many times as needed; remove this line when done)