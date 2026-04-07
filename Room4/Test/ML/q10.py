#Which visualization shows feature relationships?
#Heatmap

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
df = pd.DataFrame(X, columns=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid'])

# Correlation heatmap shows relationships between all feature pairs
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.show()