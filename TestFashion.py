
import tensorflow as tf
from tensorflow import keras

#from keras.models import load_model
#from keras.models import model_from_json﻿





jsonFile = open("Fashion.json", "r")
loadedModelJson = jsonFile.read()
jsonFile.close()

loadedModel = tf.keras.models.model_from_json(loadedModelJson)

loadedModel.load_weights("Fashion.h5")



loadedModel.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])




fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()


test_loss, test_acc = loadedModel.evaluate(test_images, test_labels)


print('Точность после проверки:', test_acc)