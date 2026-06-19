import pandas as pd

df = pd.read_csv("../Dataset/wafer_data.csv")

print(df.info())

print(df["Good/Bad"].value_counts())

print(df.isnull().sum().sort_values(ascending=False).head(20))

print(df.describe())

# Tính tỷ lệ thiếu dữ liệu
missing_percent = df.isnull().mean() * 100

print(missing_percent.sort_values(ascending=False).head(20))
