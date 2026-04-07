#Fix the Logistic Regression training mistake.

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

model = LogisticRegression

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', model)
])

pipe.fit(X_train, y_train)

