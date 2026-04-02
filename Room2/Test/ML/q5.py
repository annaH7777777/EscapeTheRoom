#Which method drops duplicates in pandas?
#drop_duplicates()
import pandas as pd

df = pd.DataFrame({
    "A": [1, 1, 2],
    "B": [3, 3, 4]
})
print(df.drop_duplicates())