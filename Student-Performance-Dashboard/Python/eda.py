import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("../Dataset/cleaned/cleaned_students.csv")


# Average Score Distribution

plt.figure(figsize=(8,5))
plt.hist(df["average_score"], bins=20)

plt.title("Average Score Distribution")
plt.xlabel("Average Score")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.savefig("../Screenshots/score_distribution.png")
plt.close()


# Average Score by Gender

gender_score = df.groupby("gender")["average_score"].mean()

plt.figure(figsize=(6,4))
plt.bar(gender_score.index, gender_score.values)

plt.title("Average Score by Gender")
plt.ylabel("Average Score")

plt.tight_layout()
plt.savefig("../Screenshots/gender_scores.png")
plt.close()


# Average Score by Lunch

lunch_score = df.groupby("lunch")["average_score"].mean()

plt.figure(figsize=(6,4))
plt.bar(lunch_score.index, lunch_score.values)

plt.title("Average Score by Lunch Type")
plt.ylabel("Average Score")

plt.tight_layout()
plt.savefig("../Screenshots/lunch_scores.png")
plt.close()

# Test Preparation Course

prep_score = df.groupby(
    "test_preparation_course"
)["average_score"].mean()

plt.figure(figsize=(6,4))
plt.bar(prep_score.index, prep_score.values)

plt.title("Average Score by Test Preparation")
plt.ylabel("Average Score")

plt.tight_layout()
plt.savefig("../Screenshots/test_preparation.png")
plt.close()

# Parental Education

parent_score = df.groupby(
    "parental_level_of_education"
)["average_score"].mean()

parent_score = parent_score.sort_values()

plt.figure(figsize=(10,5))
plt.bar(parent_score.index, parent_score.values)

plt.xticks(rotation=30)

plt.title("Average Score by Parents Education")
plt.ylabel("Average Score")

plt.tight_layout()
plt.savefig("../Screenshots/parent_education.png")
plt.close()

print("EDA completed successfully!")
print("Charts saved in Screenshots folder.")
