# Q6 (ML): What is a softmax function used for?
# Answer: Multi-class classification

import numpy as np

# Raw scores from a model (logits) for 3 classes: cat, dog, bird
logits = np.array([2.0, 1.0, 0.1])

# Softmax converts to probabilities that sum to 1
exp_scores = np.exp(logits)
softmax = exp_scores / np.sum(exp_scores)

print(f"Logits:       {logits}")
print(f"Probabilities: {softmax.round(3)}")
print(f"Sum:          {softmax.sum():.2f}  <- always equals 1")
print(f"Predicted class: index {softmax.argmax()}  (highest probability)")
