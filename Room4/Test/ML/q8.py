#Which metric measures continuous prediction error?
#MSE

from sklearn.metrics import mean_squared_error

y_true = [3.0, 5.0, 2.5, 7.0]
y_pred = [2.8, 5.2, 2.1, 6.5]

mse = mean_squared_error(y_true, y_pred)
print("MSE:", mse)  # average of squared differences