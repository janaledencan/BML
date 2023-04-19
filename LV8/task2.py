#Zadatak 8.4.2 Napišite skriptu koja ce ucitati izgradenu mrežu iz zadatka 1 i MNIST skup
#podataka. Pomocu matplotlib biblioteke potrebno je prikazati nekoliko loše klasificiranih slika iz
#skupa podataka za testiranje. Pri tome u naslov slike napišite stvarnu oznaku i oznaku predvidenu
#mrežom.

import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
import tensorflow as tf


      
# ucitavanje MNIST dataset-a
mnist = keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Postavljanje pixel-a ns vrijednosti izmedu 0 i 1
train_images = train_images / 255.0
test_images = test_images / 255.0

# ucitavanje mreze iz proslog zad
model = tf.keras.models.load_model('epic_num_reader.model/')

# predviđene oznake za testne slike
predictions = model.predict(test_images)

# pronalazak slika koje su loše klasificirane
misclassified_indices = np.where(np.argmax(predictions, axis=1) != test_labels)[0]

# prikaz 10 loše klasificiranih slika
for i in range(10):
    index = misclassified_indices[i]
    image = test_images[index]
    predicted_label = np.argmax(predictions[index])
    actual_label = test_labels[index]
    plt.subplot(2, 5, i+1)
    plt.imshow(image, cmap=plt.cm.binary)
    plt.title(f"Actual: {actual_label}\nPredicted: {predicted_label}")
    plt.xticks([])
    plt.yticks([])
plt.show()