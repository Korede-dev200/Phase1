import pandas as pd
import numpy as np

data = {
    "student": ["Ama", "Ben", "Chidi", "Dara", "Eze", "Funke"],
    "subject": ["Math", "Math", "Science", "Science", "Math", "Science"],
    "score": [78, 92, 65, 88, 55, 71],
    "attempts": [1, 1, 2, 1, 3, 2],
}
df = pd.DataFrame(data)

print(df)

# FILTERING — "which students took more than one attempt?"
print("\n")
print(df[df["attempts"] > 1])

# GROUPING — "average score per subject?"
print("\n")
print(df.groupby("subject")["score"].mean())

# SELECTING — "show me Dara's row"
print("\n")
print(df.loc[3])

# NEW COLUMN — "mark each student as a retaker"
df["retaker"] = df["attempts"] > 1

print("\n")
print(df)

print("\n")
print(df[df["score"] > 70])

df["percentage"] = df["score"].astype(str) + "%"
print(df)

# Knowing the row number of the person with the highest score in case of any new additions
print(df["score"].idxmax())

# Selecting the row with the highest score
print(df.loc[df["score"].idxmax()])

# GROUPING — "average score per subject?" and selecting the highest average
print("\n")
subject_avg = df.groupby("subject")["score"].mean()
print(subject_avg)
print(subject_avg.idxmax())


print(df["subject"].value_counts())