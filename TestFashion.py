
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




im = cv2.imread("ans.jpg")

resized = cv2.resize(im, (28, 28), interpolation = cv2.INTER_AREA)


s1 = []

for i in resized:
	s = []
	
	for j in i:
		#k = (j[0]+j[1]+j[2])/3
		s.append(255-j[1])

	s1.append(s)
	



gg = np.array(s1)

#print(gg)


test  = np.array([gg])


pred = loadedModel.predict(test)


k = np.argmax(pred[0])

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

print(class_names[k])