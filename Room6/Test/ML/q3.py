# Q3 (ML): What is precision?
# Answer: TP / (TP + FP)

from sklearn.metrics import precision_score, recall_score, confusion_matrix

# Simulated predictions
y_true = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
y_pred = [1, 1, 0, 0, 1, 0, 0, 0, 0, 0]

# Confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
print("=== Confusion Matrix ===")
print(f"  TP={tp}  FP={fp}")
print(f"  FN={fn}  TN={tn}")

# Manual calculation
print("\n=== Precision (manual) ===")
precision_manual = tp / (tp + fp)
print(f"  TP / (TP + FP) = {tp} / ({tp} + {fp}) = {precision_manual:.2f}")
print(f"  Meaning: of {tp+fp} predicted positives, {tp} were correct")

# Sklearn calculation
print(f"\n=== Precision (sklearn) ===")
print(f"  precision_score = {precision_score(y_true, y_pred):.2f}")

# Comparison with Recall
print("\n=== Precision vs Recall ===")
recall_manual = tp / (tp + fn)
print(f"  Precision = TP/(TP+FP) = {precision_manual:.2f}  'How accurate are positive predictions?'")
print(f"  Recall    = TP/(TP+FN) = {recall_manual:.2f}  'How many positives did we find?'")

# Quick memory trick
print("\n=== Memory trick ===")
print("  Precision -> FP matters -> 'Don't cry wolf' (avoid false alarms)")
print("  Recall    -> FN matters -> 'Don't miss any' (find all positives)")