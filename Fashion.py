from __future__ import absolute_import, division, print_function, unicode_literals

# Импортируем TensorFlow и tf.keras
import tensorflow as tf
from tensorflow import keras

# А также добавим вспомогательные библиотеки для вычислений и вывода данных на экран
import numpy as np
import matplotlib.pyplot as plt


fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

'''
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

print("Train_images: ", train_images.shape)

print("len(train_labels): ",len(train_labels))

print("train_labels: ", train_labels)

print("test_images.shape: ", test_images.shape)

print("len(test_labels): ", len(test_labels))

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()
'''

train_images = train_images / 255.0

test_images = test_images / 255.0


'''
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
'''

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

#model.compile(optimizer=tf.train.AdamOptimizer(), 
 #             loss='sparse_categorical_crossentropy',
 #             metrics=['accuracy'])

model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])



model.fit(train_images, train_labels, epochs=5)



test_loss, test_acc = model.evaluate(test_images, test_labels)



print('Точность после проверки:', test_acc)


model_json = model.to_json()

json_file = open("Fashion.json", "w")
json_file.write(model_json)
json_file.close()

model.save_weights("Fashion.h5")