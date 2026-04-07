#Which library is used for deep learning?
#tensorflow

# TensorFlow + Keras (Google)
import tensorflow as tf
from tensorflow import keras

model = keras.Sequential([
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model.build(input_shape=(None, 784))
model.summary()