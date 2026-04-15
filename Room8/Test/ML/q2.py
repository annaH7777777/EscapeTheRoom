# Q2: What does fit() mean in sklearn?
# Options:
#   - Predicting
#   - Training the model
#   - Splitting data
#   - Checking shape
# Answer: Training the model
#
# Explanation:
# In scikit-learn, every estimator has a .fit(X, y) method.
# fit() = TRAIN: the model looks at the data and learns its parameters
#         (e.g. coefficients for linear regression, splits for a tree).
# After fitting, you use:
#   - .predict(X_new)  -> make predictions on new data
#   - .score(X, y)     -> evaluate on labeled data
# Splitting data is done by train_test_split (separate utility),
# and "checking shape" is just X.shape — nothing to do with fit().


import numpy as np
from sklearn.linear_model import LinearRegression

# Toy data: y = 2*x + 1
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([3, 5, 7, 9, 11])

model = LinearRegression()

print(f"Before fit: coef_ attribute exists? {hasattr(model, 'coef_')}")

model.fit(X, y)              # <-- training: learns slope and intercept

print(f"After  fit: coef_      = {model.coef_}")         # ~ [2.]
print(f"After  fit: intercept_ = {model.intercept_}")    # ~ 1.0

# Use the trained model to predict
print(f"predict([[6]]) = {model.predict([[6]])}")        # ~ [13.]
