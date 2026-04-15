# Q6: Which module contains LogisticRegression?
# Options:
#   - preprocessing
#   - ensemble
#   - linear_model
#   - metrics
# Answer: linear_model
#
# Explanation:
# LogisticRegression lives in sklearn.linear_model. Despite its name,
# it's a CLASSIFICATION model — it's linear in the features but passes
# the result through a sigmoid/softmax to output class probabilities.
#
# Quick map of the other modules:
#   - sklearn.preprocessing -> scalers/encoders (StandardScaler, OneHotEncoder)
#   - sklearn.ensemble      -> RandomForest, GradientBoosting, VotingClassifier
#   - sklearn.metrics       -> accuracy_score, confusion_matrix, roc_auc_score, ...


from sklearn.linear_model import LogisticRegression  # <-- correct import
import numpy as np

# Tiny 2-class dataset
X = np.array([[0, 0], [0, 1], [1, 0], [5, 5], [6, 5], [5, 6]])
y = np.array([0, 0, 0, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)

print(f"Module : {LogisticRegression.__module__}")   # sklearn.linear_model...
print(f"coef_  : {model.coef_}")
print(f"predict([[1, 1], [6, 6]]) = {model.predict([[1, 1], [6, 6]])}")
print(f"predict_proba([[1, 1]])   = {model.predict_proba([[1, 1]])}")
