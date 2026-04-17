#Write a function that standardizes only the numeric columns of a pandas DataFrame (ignoring categorical ones).
#Note: Use df.select_dtypes and StandardScaler

import pandas as pd
from sklearn.preprocessing import StandardScaler

def standardize_numeric(df):
    numeric_df = df.select_dtypes(include='number')
    scaler = StandardScaler()
    scaled_numeric = scaler.fit_transform(numeric_df)
    scaled_numeric_df = pd.DataFrame(scaled_numeric, columns=numeric_df.columns, index=df.index)
    result = df.copy()
    result[numeric_df.columns] = scaled_numeric_df
    return result

if __name__ == "__main__":
    data = {
        'a': [1, 2, 3, 4],
        'b': [10.0, 20.0, 30.0, 40.0],
        'c': ['x', 'y', 'z', 'w'],
        'd': [100, 200, 300, 400]
    }
    df = pd.DataFrame(data)
    print(standardize_numeric(df))
