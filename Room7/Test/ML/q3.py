# Q3 (ML): What does confusion matrix diagonal represent?
# Answer: Correct predictions

import numpy as np
from sklearn.metrics import confusion_matrix

y_true = [0, 0, 0, 1, 1, 1, 2, 2, 2]
y_pred = [0, 0, 1, 1, 1, 2, 2, 2, 0]

cm = confusion_matrix(y_true, y_pred)
print(f"Confusion matrix:\n{cm}")
print(f"\nDiagonal (correct): {np.diag(cm)}")
print(f"Total correct:      {np.trace(cm)}  <- sum of diagonal")
print(f"Total predictions:  {cm.sum()}")
print(f"Accuracy:           {np.trace(cm) / cm.sum():.2f}")
