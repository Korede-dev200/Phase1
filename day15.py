import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report

np.random.seed(0)
n = 2000

temperature = np.random.normal(70, 10, n)
vibration = np.random.normal(5, 2, n)
pressure = np.random.normal(100, 15, n)
runtime_hours = np.random.uniform(0, 5000, n)

# failure becomes more likely with high temp, high vibration, long runtime
failure_score = (
    0.03 * (temperature - 70) +
    0.5 * (vibration - 5) +
    0.0006 * runtime_hours +
   np.random.normal(0, 1, n)
)
failure = (failure_score > 2).astype(int)

df = pd.DataFrame({
    "Temperature": temperature,
    "Vibration": vibration,
    "Pressure": pressure,
    "Runtime Hours": runtime_hours,
    "Failure": failure
})

print(df.head())
print(f"\nFailure rate: {df['Failure'].mean():.2%}")

X = df[["Temperature", "Vibration", "Pressure", "Runtime Hours"]]
y = df["Failure"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

model = XGBClassifier(random_state=0)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions):.4f}")
print("\n", classification_report(y_test, predictions))

# ratio of negative to positive examples in training data
neg, pos = (y_train == 0).sum(), (y_train == 1).sum()
weight = neg / pos
print(f"scale_pos_weight: {weight:.2f}")

model_weighted = XGBClassifier(random_state=0, scale_pos_weight=weight)
model_weighted.fit(X_train, y_train)

predictions_weighted = model_weighted.predict(X_test)
print(f"\nAccuracy: {accuracy_score(y_test, predictions_weighted):.4f}")
print("\n", classification_report(y_test, predictions_weighted))