#Fix the sklearn pipeline code so it runs without error and fits the model properly.

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipe = Pipeline([StandardScaler(), LogisticRegression()])
pipe.fit(X, y)
print("Pipeline trained successfully.")
#You can use this one to check print(pipe.predict([X[0]])). It will output a predicted class label like [0], [1], etc.