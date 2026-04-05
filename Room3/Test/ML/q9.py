#What is early stopping?
#Stopping training to prevent overfitting

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping

# Sample data
X_train = np.random.rand(100, 5)
y_train = np.random.randint(0, 2, 100)
X_val = np.random.rand(20, 5)
y_val = np.random.randint(0, 2, 20)

# Simple model
model = Sequential([
    Dense(16, activation='relu', input_shape=(5,)),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy')

early_stop = EarlyStopping(
    monitor='val_loss',   # watch validation loss
    patience=3,           # stop after 3 epochs of no improvement
    restore_best_weights=True  # go back to best epoch
)

model.fit(X_train, y_train,
          epochs=1000,         # set high — early stopping will cut it
          callbacks=[early_stop],
          validation_data=(X_val, y_val))