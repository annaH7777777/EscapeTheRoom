# What does .iloc[] access?
# Rows by index

import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B", "C"]
})
print(df.iloc[0])   # first row