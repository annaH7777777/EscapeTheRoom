#Which method splits train/test data in sklearn?
#train_test_split

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Train size: {len(X_train)}")  # → 120
print(f"Test size: {len(X_test)}")    # → 30