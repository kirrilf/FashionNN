
import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2







jsonFile = open("Fashion.json", "r")
loadedModelJson = jsonFile.read()
jsonFile.close()

loadedModel = tf.keras.models.model_from_json(loadedModelJson)

loadedModel.load_weights("Fashion.h5")



loadedModel.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])






fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()


#test1  = np.array([test_images[6]])


#pred1 = loadedModel.predict(test1)


#print("GG: ", np.argmax(pred1[0]))



im = cv2.imread("8.jpg")

resized = cv2.resize(im, (28, 28), interpolation = cv2.INTER_AREA)


s1 = []

for i in resized:
	s = []
	
	for j in i:
		#k = (j[0]+j[1]+j[2])/3
		s.append(255-j[0])

	s1.append(s)
	

gg = np.array(s1)
#print(gg)

test  = np.array([gg])


pred = loadedModel.predict(test)


print("TT: ", np.argmax(pred[0]))

#print(test_images[0])

#print("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")

#print(gg)
