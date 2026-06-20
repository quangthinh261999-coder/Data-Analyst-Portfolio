import pandas as pd

df = pd.read_csv("../Dataset/wafer_data_clean.csv")

# Chỉ lấy các cột sensor

sensor_cols = [col for col in df.columns if "Sensor" in col]

# Tính độ lệch chuẩn

sensor_std = df[sensor_cols].std()

print(
    sensor_std
    .sort_values(ascending=False)
    .head(20)
)


print("\n")

print(
    df["Good/Bad"]
    .value_counts(normalize=True) * 100
)
