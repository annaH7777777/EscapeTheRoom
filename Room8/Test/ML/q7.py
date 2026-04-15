# Q7: What does accuracy measure?
# Options:
#   - True Positives / Total
#   - All correct predictions / total predictions
#   - True negatives only
#   - True positives only
# Answer: All correct predictions / total predictions
#
# Explanation:
# Accuracy = (TP + TN) / (TP + TN + FP + FN)
#          = number of correct predictions / total predictions
# It counts BOTH correctly predicted positives AND correctly predicted
# negatives. "TP / Total" is not a standard metric; precision and recall
# focus on positives specifically.
#
# Caveat: accuracy is misleading on imbalanced datasets. If 95% of
# samples are class 0, a dumb "always predict 0" model gets 95% accuracy
# but is useless — use precision, recall, F1, or ROC-AUC instead.


import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix

y_true = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 0])
y_pred = np.array([1, 0, 1, 0, 0, 1, 1, 0, 1, 0])    # 2 mistakes out of 10

acc_sklearn = accuracy_score(y_true, y_pred)
acc_manual  = (y_true == y_pred).sum() / len(y_true)

print(f"accuracy_score(y_true, y_pred) = {acc_sklearn}")
print(f"manual correct/total           = {acc_manual}")

# Break it down with a confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
print(f"TP={tp}, TN={tn}, FP={fp}, FN={fn}")
print(f"(TP + TN) / Total = ({tp} + {tn}) / {len(y_true)} = {(tp + tn) / len(y_true)}")
