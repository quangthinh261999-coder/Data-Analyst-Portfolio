import pandas as pd

data = {
    "Sensor": [
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
    ],
    "Difference": [
        4376,
        2106,
        1100,
        1043,
        478,
        402,
        376,
        251,
        209,
        183
    ]
}

df = pd.DataFrame(data)

df.to_csv(
    "../Dataset/top_sensors.csv",
    index=False
)

print(df)
