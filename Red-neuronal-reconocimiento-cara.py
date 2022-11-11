import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K

from keras.models import load_model
model_new = load_model("clasificadormodelobueno.h5")

img_width, img_height = 178, 218

train_data_dir = 'cara'
validation_data_dir = 'cara'
nb_train_samples = 500
nb_validation_samples = 336
epochs = 100
batch_size = 32

if K.image_data_format() == 'primercanal':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

model_new = Sequential()
model_new.add(Conv2D(32, (3, 3), input_shape=input_shape))
model_new.add(Activation('relu'))
model_new.add(MaxPooling2D(pool_size=(2, 2)))

model_new.add(Conv2D(32, (3, 3)))
model_new.add(Activation('relu'))
model_new.add(MaxPooling2D(pool_size=(2, 2)))

model_new.add(Conv2D(64, (3, 3)))
model_new.add(Activation('relu'))
model_new.add(MaxPooling2D(pool_size=(2, 2)))

model_new.add(Flatten())
model_new.add(Dense(64))
model_new.add(Activation('relu'))
model_new.add(Dropout(0.5))
model_new.add(Dense(1))
model_new.add(Activation('sigmoid'))

model_new.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

model_new.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples // batch_size)

model_new.save_weights('segundointento.h5')


