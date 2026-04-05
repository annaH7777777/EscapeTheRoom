#You are training a Support Vector Machine (SVM) classifier on the Iris dataset. 
#Fix the incorrect model Training pipeline so it uses only the training data then test it properly on the separate test set.

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y)

model = SVC(kernel='linear', probability=True)
model.fit(X)
print(model.score(X_test, y_test))
