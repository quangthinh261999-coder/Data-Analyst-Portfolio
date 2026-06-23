

# Semiconductor Wafer Quality Dashboard

## Project Overview

This project analyzes semiconductor wafer sensor data to identify factors related to wafer quality.

## Tools Used

- Python (Pandas)
- Power BI
- GitHub

## Dataset

- 101 wafers
- 590 sensor measurements
- Quality label (Good / Bad)

## Data Cleaning

- Removed 16 sensors with excessive missing values
- Created cleaned dataset for dashboarding

## Key Insights
- The wafer production dataset is highly imbalanced, with only 6% good wafers.
- Only 5.94% of wafers were classified as Good
- Sensor-298 ranked second among critical sensor.
- Sensor-163 exhibits the largest performance gap between good and bad wafers, indicating a potential relationship with wafer quality.

## Dashboard Pages

### Page 1 - Overview

- Total Wafers
- Good Wafers
- Bad Wafers
- Yield Rate
- Quality Distribution
- 
<img width="1262" height="670" alt="page1_dashboard_overview" src="https://github.com/user-attachments/assets/58f66f7b-26cf-4a22-9e0c-44138e176d81" />
### Page 2 - Sensor Analysis

- Top Critical Sensors
- Sensor-163 Comparison
- Sensor-298 Comparison

<img width="1263" height="663" alt="page2_sensor_analysis" src="https://github.com/user-attachments/assets/46dc1ab8-e87c-4d33-bf5c-8e6fbd46ee00" />



