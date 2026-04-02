#Which method fills missing values?
#fillna()
import pandas as pd

df = pd.DataFrame({
    "A": [1, None, 3]
})

print(df.fillna(0))