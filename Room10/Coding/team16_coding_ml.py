#Write a function standardize_and_classify(df) that accepts a pandas DataFrame with numerical columns ["A", "B"]
#and target column "label"; standardizes the columns ["A", "B"] using StandardScaler;
#fits a LogisticRegression model to classify "label", returns the model's training accuracy using .score().

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

def standardize_and_classify(df):
    X = df[["A", "B"]]
    y = df["label"]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    model = LogisticRegression()
    model.fit(X_scaled, y)
    return model.score(X_scaled, y)

if __name__ == "__main__":
    data = {
        "A":     [1, 2, 3, 10, 11, 12],
        "B":     [2, 1, 3, 11, 12, 10],
        "label": [0, 0, 0,  1,  1,  1],
    }
    df = pd.DataFrame(data)
    accuracy = standardize_and_classify(df)
    print(f"Training accuracy: {accuracy:.2f}")
