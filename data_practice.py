import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# deliberately messy data
data = {
    "student": [" Ana ", "Ben", "Ana", "Cara", "Dan"],
    "subject": ["python", "numpy", "python", "pandas", "numpy"],
    "hours": ["2", "3", "2", "bad", "5"],
    "score": [70, 85, 70, None, 95],
}

df = pd.DataFrame(data)
print("Raw Data:")
print(df)

# Clean the data
df["student"] = df["student"].str.strip()
df["subject"] = df["subject"].str.title()
df["hours"] = pd.to_numeric(df["hours"], errors="coerce")
df["hours"] = df["hours"].fillna(df["hours"].median())
df["score"] = df["score"].fillna(df["score"].median())
df = df.drop_duplicates()

print("\nClean data:")
print(df)

# NumPy calculations
hours = df["hours"].to_numpy()

print("\nNumPy statistics:")
print("Average hours:", np.mean(hours))
print("Most hours:", np.max(hours))
print("Above-average hours:", hours[hours > np.mean(hours)])

# Pandas analysis
subject_scores = df.groupby("subject")["score"].mean()

print("\nAverage score by subject:")
print(subject_scores)

# Visualization
subject_scores.plot(
    kind="bar",
    title="Average Score by Subject",
    color="cornflowerblue",
)

plt.xlabel("Subject")
plt.ylabel("Average score")
plt.tight_layout()
plt.savefig("subject_scores.png")
plt.show()