# Q10 (ML): What technique combines multiple models?
# Answer: Stacking

from sklearn.datasets import load_iris
from sklearn.ensemble import StackingClassifier, BaggingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

X, y = load_iris(return_X_y=True)

# === STACKING: different models combined via meta-learner ===
stacking = StackingClassifier(
    estimators=[
        ("tree", DecisionTreeClassifier()),
        ("knn", KNeighborsClassifier()),
    ],
    final_estimator=LogisticRegression()  # meta-learner
)
stacking.fit(X, y)
print(f"Stacking score: {stacking.score(X, y):.3f}  (combines different model types)")

# === BAGGING: same model, multiple instances ===
bagging = BaggingClassifier(estimator=DecisionTreeClassifier(), n_estimators=10)
bagging.fit(X, y)
print(f"Bagging score:  {bagging.score(X, y):.3f}  (multiple trees on different samples)")

print("\n=== Ensemble methods summary ===")
print("  Bagging  -> many copies of SAME model (e.g., Random Forest)")
print("  Boosting -> models trained sequentially to fix predecessors' errors")
print("  Stacking -> DIFFERENT models + meta-learner to combine them")
