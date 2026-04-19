#Fix the code to train the model and predict on the same features.

import pandas as pd
from sklearn.linear_model import LogisticRegression

def classify_data():
    data = pd.DataFrame({
        "x": [1, 2, 3],
        "y": [4, 5, 6],
        "label": [0, 1, 0]
    })
    model = LogisticRegression()
    model.fit(data[["x", "y"]], data["label"])
    predictions = model.predict(data[["x", "y"]])
    if len(predictions) == 3:
        return "Model complete"
    else:
        return "Try again"

print(classify_data())