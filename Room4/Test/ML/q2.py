#What is a confusion matrix?
#Matrix for classification performance

from sklearn.metrics import confusion_matrix

y_true = [1, 0, 1, 1, 0, 1, 0, 0]
y_pred = [1, 0, 1, 0, 0, 1, 1, 0]

cm = confusion_matrix(y_true, y_pred)
print(cm)
# → [[3, 1],
#    [1, 3]]
