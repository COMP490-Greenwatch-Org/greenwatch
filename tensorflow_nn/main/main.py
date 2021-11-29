import matplotlib.pyplot as plt
import numpy as np
import os
import shutil
import PIL
import tensorflow as tf
import pathlib
import pandas as pd

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.python.data.ops.dataset_ops import AUTOTUNE;

from datetime import datetime

image_height = 256
image_width = 256
batch_size = 32
num_classes = 2

def w(x: str):
    if x == 'TRUE':
        return 1
    return 0

traindf = pd.read_csv('./tensorflow_nn/test_dataset.csv', dtype=str, converters={1: w});

for row in traindf.itertuples():
    filename = 'tensorflow_nn/test_dataset/unsorted/' + row._1
    dest: str;
    if (row._2 == 1):
        dest = 'tensorflow_nn/test_dataset/images/healthy'
    else:
        dest = 'tensorflow_nn/test_dataset/images/unhealthy'
    shutil.copy2(filename, dest)

train_ds = image_dataset_from_directory(
    'tensorflow_nn/test_dataset/images',
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(image_height,image_width),
    batch_size=batch_size
)

val_ds = image_dataset_from_directory(
    'tensorflow_nn/test_dataset/images',
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(image_height,image_width),
    batch_size=batch_size
)

AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().take(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

data_augmentation = keras.Sequential(
  [
    layers.RandomFlip("horizontal",
                      input_shape=(image_height,
                                  image_width,
                                  3)),
    #layers.RandomRotation(0.2),
    layers.RandomZoom(0.1),
  ]
)

plt.figure(figsize=(20, 20))
for images, _ in train_ds.take(2):
  for i in range(9):
    augmented_images = data_augmentation(images)
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(augmented_images[0].numpy().astype("uint8"))
    plt.axis("off")
plt.savefig('image_augmentation_' + datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") + '.png');


""" model = Sequential([
    data_augmentation,
    layers.Rescaling(1./255, input_shape=(image_height, image_width, 3)),
    layers.Conv2D(16, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(32, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(num_classes)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.summary()

epochs=10
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs
)

#model.save('tensorflow_nn/models/model_' + datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p"), save_format="h5")

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.savefig('training_val_loss_' + datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") + '.png');
 """