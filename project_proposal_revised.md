#### SER594: Project Proposal
#### Room Occupancy Estimation
#### Akshata Bharadwaj Kodagnur
#### 10/30/2023


**Keywords:**  Sensor data, Air quality, Room occupancy

**Description:**
I had earlier done some projects on calculating the Indoor Air Quality Index (AQI) based on the concentration of various pollutants
like NO2, CO, CO2 etc. This is one step further, 
wherein I can determine the number of people that can occupy a room based on the air quality of the room. This can be done using Support Vector Machine and Random Forest algorithm.
The dataset would include the sensor readings of pollutants, humidity and temperature levels.
Some of the questions we can ask would be: 
1. How good is the air quality of the room? This would give us 
some insight on how many people can be in the room to maintain safe level of AQI.
2. What can be done to improve the air quality? Based on which pollutant is causing the air quality issue,
there are different corrective actions that can be taken to mitigate the risks of bad air quality.

**Research Questions:**

1. To describe the trends within the readings obtained from different types of sensors. 

2. To predict the number of people that can occupy a room based on the temperature, Carbon dioxide concentration, sound, light and motion sensor readings.

3. To defend the model in performing the prediction of room occupancy.

4. To evaluate causal relationships implied by the room occupancy model.

**Intellectual Merit:** I have come across some studies that are doing the room occupancy estimation. 
But I would also want to focus on finding the pollutant that is key contributor to this estimation
based on the trends. Large number of occupants in the room are sources of CO2 themselves,
hence it is necessary to maintain a safe number. Instead of using cameras, RFIDs and wifi, data is collected by a bunch of sensors.

**Data Sourcing:** I found this dataset, which has been shared recently in 2023. There are columns for CO2, sound, light, temperature and passive infrared(PIR) readings.
This would be a good place to start. 
http://archive.ics.uci.edu/dataset/864/room+occupancy+estimation


**Background Knowledge:**
1. https://www.ashrae.org/file%20library/about/position%20documents/pd_indoorcarbondioxide_2022.pdf
2. https://www.astm.org/d6245-12.html
3. https://www.energy.wsu.edu/Portals/0/Documents/Measuring_CO2_Inside_Buildings-Jan2013.pdf
4. [How to Predict Room Occupancy Based on Environmental Factors](https://machinelearningmastery.com/how-to-predict-room-occupancy-based-on-environmental-factors/)
5. [Smart occupancy sensors to reduce energy consumption](https://www.sciencedirect.com/science/article/pii/S0378778899000407?casa_token=zkLQKBqlO5QAAAAA:gGAwxiavX79ks3i-igNN7FWAtG1sllEVajgHpXgdiWUrs4NZ7pZQ4Tp0h7m5kNQvgzqaxbmoDQ)


**Related Work:** 
1.  AP Singh, V. Jain, S. Chaudhari, F. A. Kraemer, S. Werner and V. Garg, "Machine Learning-Based Occupancy Estimation Using Multivariate Sensor Nodes," 2018 IEEE Globecom Workshops (GC Wkshps), Abu Dhabi, United Arab Emirates, 2018, pp. 1-6, doi: 10.1109/GLOCOMW.2018.8644432.
https://ieeexplore-ieee-org.ezproxy1.lib.asu.edu/document/8644432

2. https://search.lib.asu.edu/permalink/01ASU_INST/fdcm53/cdi_pubmed_primary_36679383

3. https://www.nist.gov/publications/indoor-carbon-dioxide-metric-analysis-tool

4. https://doi.org/10.1109/PERCOMW.2016.7457116

5. https://doi-org.ezproxy1.lib.asu.edu/10.1016/j.enbuild.2015.11.071

6. https://dl-acm-org.ezproxy1.lib.asu.edu/doi/10.5555/2048536.2048555