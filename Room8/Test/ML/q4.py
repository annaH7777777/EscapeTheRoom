# Q4: What type of model is DecisionTreeClassifier?
# Options:
#   - Clustering
#   - Classification
#   - Regression
#   - Normalization
# Answer: Classification
#
# Explanation:
# The name gives it away: "...Classifier" -> classification task
# (predicts a discrete class label). For predicting a numeric value
# you'd use DecisionTreeRegressor instead.
# Sklearn's naming convention:
#   - *Classifier -> classification (predict class label)
#   - *Regressor  -> regression     (predict numeric value)
# Clustering (e.g. KMeans) and normalization (e.g. MinMaxScaler,
# StandardScaler) are different categories of tools.


import numpy as np
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor

# Features
X = np.array([[1, 1], [1, 2], [2, 1], [6, 6], [7, 7], [6, 7]])

# Classification: discrete labels
y_class = np.array(["A", "A", "A", "B", "B", "B"])
clf = DecisionTreeClassifier(random_state=0)
clf.fit(X, y_class)
print(f"Classifier predictions: {clf.predict([[2, 2], [7, 6]])}")   # ['A' 'B']
print(f"Classifier classes_:    {clf.classes_}")

# For contrast: DecisionTreeRegressor predicts numeric values
y_num = np.array([1.0, 1.2, 1.1, 9.0, 9.5, 9.1])
reg = DecisionTreeRegressor(random_state=0)
reg.fit(X, y_num)
print(f"Regressor  predictions: {reg.predict([[2, 2], [7, 6]])}")   # numeric
