import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("../Dataset/raw/StudentsPerformance.csv")

# Hiển thị 5 dòng đầu
print(df.head())

# Kích thước dữ liệu
print("\nShape:")
print(df.shape)

print("\n========== DATA INFO ==========")
print(df.info())

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DESCRIPTIVE STATISTICS ==========")
print(df.describe())

print("\n========== UNIQUE VALUES ==========")

for col in df.columns:
    print(f"{col}: {df[col].nunique()} unique values")

# Chuẩn hóa tên cột
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("/", "_")
)

print("\n========== NEW COLUMN NAMES ==========")
print(df.columns.tolist())

score_columns = [
    "math_score",
    "reading_score",
    "writing_score"
]

df["average_score"] = df[score_columns].mean(axis=1)
df["total_score"] = df[score_columns].sum(axis=1)
df["status"] = df["average_score"].apply(
    lambda x: "Pass" if x >= 50 else "Fail"
)


score_columns = [
    "math_score",
    "reading_score",
    "writing_score"
]

df["average_score"] = df[score_columns].mean(axis=1)

df["total_score"] = df[score_columns].sum(axis=1)

def performance(score):
    if score >= 85:
        return "Excellent"
    elif score >= 70:
        return "Good"
    elif score >= 50:
        return "Average"
    else:
        return "Poor"

df["performance_level"] = df["average_score"].apply(performance)

print(df.head())

print("\nStatus Distribution:")
print(df["status"].value_counts())

print("\nPerformance Distribution:")
print(df["performance_level"].value_counts())



df.to_csv(
    "../Dataset/cleaned/cleaned_students.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")


