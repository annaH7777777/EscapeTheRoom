#Which method selects top k features?
#SelectKBest

from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
print("Original features:", X.shape[1])  # 4

selector = SelectKBest(score_func=f_classif, k=2)
X_selected = selector.fit_transform(X, y)
print("Selected features:", X_selected.shape[1])  # 2

print("Feature scores:", selector.scores_)
print("Selected mask:", selector.get_support())