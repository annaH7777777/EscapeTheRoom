# Q6: What is the purpose of encoding categorical variables?
# Options:
#   - Normalize them
#   - Drop them
#   - Make them numeric
#   - Visualize them
# Answer: Make them numeric
#
# Explanation:
# ML models work with NUMBERS, not strings. Categorical values like
# "red" / "green" / "blue" must be converted to numeric form before
# training. Common encodings:
#   - Label / Ordinal encoding → map each category to an integer
#     (e.g. red=0, green=1, blue=2). Good when the categories really
#     have an order (e.g. "low" < "medium" < "high"); MISLEADING for
#     unordered categories because integers imply magnitude/ordering.
#   - One-hot encoding → create a separate 0/1 column per category.
#     Preferred for unordered ("nominal") features; no fake ordering.
# Normalizing or visualizing are DIFFERENT preprocessing steps; dropping
# the column throws information away.


import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

colors = np.array(["red", "green", "blue", "green", "red", "blue"]).reshape(-1, 1)

# --- Label encoding: each category → one integer ---
le = LabelEncoder()
label_encoded = le.fit_transform(colors.ravel())
print(f"Categories      : {le.classes_.tolist()}")      # ['blue', 'green', 'red']
print(f"Label encoded   : {label_encoded.tolist()}")    # e.g. [2, 1, 0, 1, 2, 0]

# --- One-hot encoding: each category → its own 0/1 column ---
ohe = OneHotEncoder(sparse_output=False)
one_hot = ohe.fit_transform(colors)
print(f"One-hot columns : {ohe.get_feature_names_out().tolist()}")
print(f"One-hot matrix  :\n{one_hot.astype(int)}")

# After encoding, the data is numeric and ready for sklearn models
print(f"Result dtype    : {one_hot.dtype}")             # float64, numeric
