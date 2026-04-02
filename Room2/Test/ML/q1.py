#Which function is used for one-hot encoding in pandas?
# pd.get_dummies()
import pandas as pd

df = pd.DataFrame({
    "color": ["red", "blue", "red"]
})

print(pd.get_dummies(df))