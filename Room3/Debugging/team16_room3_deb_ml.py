#You are training a Support Vector Machine (SVM) classifier on the Iris dataset. 
#Fix the incorrect model Training pipeline so it uses only the training data then test it properly on the separate test set.

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
print("Full dataset shape:", X.shape, y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y)
print("Train shape:", X_train.shape, y_train.shape)
print("Test shape:", X_test.shape, y_test.shape)

model = SVC(kernel='linear', probability=True)
print("Model params:", model.get_params())

model.fit(X_train, y_train)
print("Training complete")
print("Support vectors shape:", model.support_vectors_.shape)
print("Number of support vectors per class:", model.n_support_)

predictions = model.predict(X_test)
print("Predictions:", predictions)
print("Actual model:", y_test)

print("Accuracy:", model.score(X_test, y_test))
