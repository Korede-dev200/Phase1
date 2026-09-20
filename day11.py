import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge, Lasso


np.random.seed(0)
n_samples = 50
n_features = 8

X = np.random.randn(n_samples, n_features)    # 50 rows, 8 random feature columns
true_coefs = np.array([5, -3, 0, 0, 0, 0, 0, 0])        # only features 0 and 1 actually matter
y = X @ true_coefs + np.random.normal(0, 1, n_samples)   # add some noise

model = LinearRegression()
model.fit(X, y)
print(np.round(model.coef_, 2))

ridge = Ridge(alpha=1.0).fit(X, y)
lasso = Lasso(alpha=0.5).fit(X, y)

print("Ridge:", np.round(ridge.coef_, 2))
print("Lasso:", np.round(lasso.coef_, 2))