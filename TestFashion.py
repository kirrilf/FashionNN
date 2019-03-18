
import tensorflow as tf
from tensorflow import keras
import numpy as np








jsonFile = open("Fashion.json", "r")
loadedModelJson = jsonFile.read()
jsonFile.close()

loadedModel = tf.keras.models.model_from_json(loadedModelJson)

loadedModel.load_weights("Fashion.h5")

loadedModel.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])





fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()



test  = np.array([test_images[6]])


pred = loadedModel.predict(test)

print(np.argmax(pred[0]))

print(test_images[0])


