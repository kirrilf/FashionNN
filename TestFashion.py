
import tensorflow as tf
from tensorflow import keras
import numpy as np



def st(s1):
	jsonFile = open("Fashion.json", "r")
	loadedModelJson = jsonFile.read()
	jsonFile.close()

	loadedModel = tf.keras.models.model_from_json(loadedModelJson)

	loadedModel.load_weights("Fashion.h5")


	loadedModel.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])


	gg = np.array(s1)

	#print(gg)


	test  = np.array([gg])


	pred = loadedModel.predict(test)


	k = np.argmax(pred[0])

	class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
	               'Sandal', 'Shirt', 'Sneaker', 'T-shirt/top', 'Ankle boot']



	return class_names[k]




