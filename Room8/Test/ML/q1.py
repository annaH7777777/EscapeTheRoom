# Q1: What is a label in supervised learning?
# Options:
#   - A feature
#   - The target/output
#   - An ID
#   - The dataset name
# Answer: The target/output
#
# Explanation:
# In supervised learning, each training sample has:
#   - features (X) — the inputs the model sees
#   - a label   (y) — the correct target/output we want the model to learn to predict
# The model learns the mapping X -> y during training.
# Examples:
#   - Spam classifier: features = email text; label = "spam" or "not spam"
#   - House price regressor: features = sqft/rooms/location; label = price


import numpy as np
from sklearn.linear_model import LogisticRegression

# Features (X): two numeric inputs per sample
X = np.array([
    [1, 2],
    [2, 1],
    [3, 3],
    [6, 7],
    [7, 8],
    [8, 6],
])

# Labels (y): the target/output for each row (0 = class A, 1 = class B)
y = np.array([0, 0, 0, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)              # the model learns X -> y (features -> label)

new_samples = np.array([[2, 2], [7, 7]])
predicted_labels = model.predict(new_samples)

print(f"Features (X) shape: {X.shape}")
print(f"Labels   (y):       {y}")
print(f"Predicted labels for {new_samples.tolist()}: {predicted_labels.tolist()}")
