import pandas as pd

df = pd.read_csv("../Dataset/wafer_data_clean.csv")

top_sensors = [
    "Sensor-163",
    "Sensor-298",
    "Sensor-25",
    "Sensor-162",
    "Sensor-297",
    "Sensor-160",
    "Sensor-4",
    "Sensor-501",
    "Sensor-226",
    "Sensor-487"
]

dashboard_df = df[
    ["Unnamed: 0", "Good/Bad"] + top_sensors
]

dashboard_df.to_csv(
    "../Dataset/dashboard_data.csv",
    index=False
)

print(dashboard_df.head())
print(dashboard_df.shape)
