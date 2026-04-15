#Write a function that calculates the mean and standard deviation for each numeric column in a pandas DataFrame.
#Note: Ignore non-numeric columns.

import pandas as pd

def mean_std_numeric(df):
    numeric_df = df.select_dtypes(include='number')
    result = pd.DataFrame({
        'mean': numeric_df.mean(),
        'std': numeric_df.std()
    })
    return result

if __name__ == "__main__":
    data = {
        'a': [1, 2, 3, 4],
        'b': [10.0, 20.0, 30.0, 40.0],
        'c': ['x', 'y', 'z', 'w'],
        'd': [100, 200, 300, 400]
    }
    df = pd.DataFrame(data)
    print(mean_std_numeric(df))
