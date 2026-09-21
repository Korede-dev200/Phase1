from sklearn.datasets import make_moons
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN

X, true_labels = make_moons(n_samples=200, noise=0.05, random_state=0)

plt.figure(figsize=(6, 5))
plt.scatter(X[:, 0], X[:, 1])
plt.title("Raw data - no clustering yet")
plt.savefig("day13_raw.png")
print("Saved!")

kmeans = KMeans(n_clusters=2, random_state=0, n_init=10)
kmeans_labels = kmeans.fit_predict(X)

plt.figure(figsize=(6, 5))
plt.scatter(X[:, 0], X[:, 1], c=kmeans_labels)
plt.title("KMeans clustering ")
plt.savefig("day13_kmeans.png")
print("Saved!")

dbscan = DBSCAN(eps=0.2, min_samples=5)
dbscan_labels = dbscan.fit_predict(X)

plt.figure(figsize=(6, 5))
plt.scatter(X[:, 0], X[:, 1], c=dbscan_labels)
plt.title("DBSCAN clustering")
plt.savefig("day13_dbscan.png")
print("Saved!")