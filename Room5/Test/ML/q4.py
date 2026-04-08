#What is recall in classification?
#Correct positive predictions / total positives

from sklearn.metrics import recall_score

y_true = [1, 1, 1, 0, 0, 1]
y_pred = [1, 0, 1, 0, 0, 1]

recall = recall_score(y_true, y_pred)
print(f"Recall: {recall:.2f}")
# 3 correct positives / 4 total positives = 0.75