# Q8: What does OneHotEncoder do?
# Options:
#   - Drops null values
#   - Encodes categorical variables
#   - Scales numerical columns
#   - Binarizes predictions
# Answer: Encodes categorical variables
#
# Explanation:
# OneHotEncoder converts each categorical column into several 0/1 columns —
# one per distinct category. For a feature "color" with values {red, green,
# blue}, it creates three binary columns: is_red, is_green, is_blue.
# Why: most ML models only accept numeric input. Naively mapping
# red=0, green=1, blue=2 would imply an ordering (blue > red), which is
# usually false for categorical data.
# Use OneHotEncoder for *nominal* features (no natural order). For *ordinal*
# features (small < medium < large) use OrdinalEncoder instead.
# The other options map to different tools:
#   - Drops null values      → df.dropna() / SimpleImputer
#   - Scales numerical cols  → StandardScaler / MinMaxScaler
#   - Binarizes predictions  → Binarizer / thresholding, not one-hot.


import numpy as np
from sklearn.preprocessing import OneHotEncoder

# A single categorical feature "color" with three possible values
X = np.array([["red"], ["green"], ["blue"], ["red"], ["blue"]])

encoder = OneHotEncoder(sparse_output=False)   # dense array, easier to print
X_encoded = encoder.fit_transform(X)

print(f"categories : {encoder.categories_}")
print(f"feature names: {encoder.get_feature_names_out(['color'])}")
print(f"\noriginal:\n{X}")
print(f"\none-hot:\n{X_encoded}")
# Each row has exactly one "1" — hence "one-hot".

# Use handle_unknown='ignore' to avoid errors on unseen categories at
# transform time (common in prod pipelines).
