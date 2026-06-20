import pandas as pd

df = pd.read_csv("../Dataset/wafer_data_clean.csv")

sensor_cols = [col for col in df.columns if "Sensor" in col]

results = []

for sensor in sensor_cols:

    good_mean = df[df["Good/Bad"] == 1][sensor].mean()

    bad_mean = df[df["Good/Bad"] == -1][sensor].mean()

    diff = abs(good_mean - bad_mean)

    results.append([sensor, diff])

result_df = pd.DataFrame(
    results,
    columns=["Sensor", "Difference"]
)

print(
    result_df
    .sort_values(
        by="Difference",
        ascending=False
    )
    .head(20)
)
