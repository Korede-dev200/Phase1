from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt


data = load_iris()
X = data.data 
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

print(X_train.shape, X_test.shape)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Logistic Regression accuracy: {accuracy: 2f}")

models = {
    "Logistic Regression": LogisticRegression(max_iter=200),
    "Decision Tree": DecisionTreeClassifier(random_state=0),
    "Random forest": RandomForestClassifier(random_state=0),
    "SVM": SVC(),
}

for name, m in models.items():
    m.fit(X_train, y_train)
    acc = accuracy_score(y_test, m.predict(X_test))
    print(f"{name:20s}: {acc:.2f}")

tree_model = DecisionTreeClassifier(random_state=0, max_depth=3)
tree_model.fit(X_train, y_train)

plt.figure(figsize=(12, 8))
plot_tree(tree_model, feature_names=data.feature_names, class_names=data.target_names, filled=True)
plt.savefig("iris_tree.png")
print("Saved!")