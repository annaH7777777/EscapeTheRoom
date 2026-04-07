#Which metric is best for imbalanced classification?
#F1 Score

from sklearn.metrics import f1_score, accuracy_score

# Imbalanced dataset: 90 negatives, 10 positives
y_true = [0]*90 + [1]*10
y_pred = [0]*100  # naive model predicts all as 0

print("Accuracy:", accuracy_score(y_true, y_pred))   # 0.9 — misleadingly high
print("F1 Score:", f1_score(y_true, y_pred))          # 0.0 — exposes the problem