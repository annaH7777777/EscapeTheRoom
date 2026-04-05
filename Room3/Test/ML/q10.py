#What is the purpose of confusion matrix?
#Compare true vs predicted classes

# Predicted
#                  No      Yes
# Actual  No  [  TN  |  FP  ]
#         Yes [  FN  |  TP  ]
#
# TN = True Negative  ✅ correctly said No
# TP = True Positive  ✅ correctly said Yes
# FP = False Positive ❌ said Yes, was No  (Type I error)
# FN = False Negative ❌ said No, was Yes  (Type II error)

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
y_pred = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]

cm = confusion_matrix(y_true, y_pred)
disp = ConfusionMatrixDisplay(cm)
disp.plot()