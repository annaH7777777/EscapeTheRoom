#What is the main idea of bagging?
#Combine weak models on different data samples

from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

model = BaggingClassifier(
    estimator=DecisionTreeClassifier(),  # ← changed from base_estimator
    n_estimators=100,
    bootstrap=True
)

print(model)