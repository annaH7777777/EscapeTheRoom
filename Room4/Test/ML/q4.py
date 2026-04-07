#Which sklearn module handles grid search?
#model_selection

from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

param_grid = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}

grid = GridSearchCV(SVC(), param_grid, cv=3, scoring='accuracy')
grid.fit(X, y)

print("Best params:", grid.best_params_)
print("Best score:", round(grid.best_score_, 3))