#Write a function that normalizes a pandas DataFrame per column, skipping columns with constant values.

import pandas as pd


def normalize_df(df):
    # Copy so we don't modify the original
    result = df.copy()
    # Process each column one by one
    for col in result.columns:
        col_min = result[col].min()
        col_max = result[col].max()
        # Skip constant columns (min == max means all values are the same)
        # This also avoids division by zero
        if col_min == col_max:
            continue
        # Min-max normalization: scales values to [0, 1]
        result[col] = (result[col] - col_min) / (col_max - col_min)
    return result


# === Test ===
df = pd.DataFrame({
    "a": [1, 2, 3, 4, 5],       # varies -> will be normalized
    "b": [10, 20, 30, 40, 50],  # varies -> will be normalized
    "c": [7, 7, 7, 7, 7]        # constant -> will be skipped
})

print("=== Original ===")
print(df)

print("\n=== Normalized ===")
print(normalize_df(df))
