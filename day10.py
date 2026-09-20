from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

data = load_iris()
print(type(data))
print(data.keys())

import pandas as pd

df = pd.DataFrame(data.data, columns=data.feature_names)
df["species"] = data.target
df["species_names"] = df["species"].map({0: "setosa", 1: "versicolor", 2: "virginica"})

print(df.head())
print(data.target_names)
print(df["species_names"].unique())

kmeans = KMeans(n_clusters=3, random_state=0, n_init=10)
df["cluster"] = kmeans.fit_predict(df[data.feature_names])

print(df.groupby(["species_names", "cluster"]).size())
