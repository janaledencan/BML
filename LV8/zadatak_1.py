import numpy as np
from tensorflow import keras
from keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
import tensorflow as tf

# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# train i test podaci
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# prikaz karakteristika train i test podataka
print('Train: X=%s, y=%s' % (x_train.shape, y_train.shape))
print('Test: X=%s, y=%s' % (x_test.shape, y_test.shape))

# TODO: prikazi nekoliko slika iz train skupa
plt.imshow(x_train[0], cmap=plt.cm.binary)
plt.imshow(x_train[1], cmap=plt.cm.binary)
plt.imshow(x_train[2], cmap=plt.cm.binary)
plt.show()

# skaliranje slike na raspon [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

# slike trebaju biti (28, 28, 1)
x_train_s = np.expand_dims(x_train_s, -1)
x_test_s = np.expand_dims(x_test_s, -1)

print("x_train shape:", x_train_s.shape)
print(x_train_s.shape[0], "train samples")
print(x_test_s.shape[0], "test samples")


# pretvori labele
y_train_s = keras.utils.to_categorical(y_train, num_classes)
y_test_s = keras.utils.to_categorical(y_test, num_classes)


# TODO: kreiraj model pomocu keras.Sequential(); prikazi njegovu strukturu

#model = tf.keras.models.Sequential() 

model = keras.Sequential()
model.add(layers.Input( shape =(784, )))
model.add(layers.Dense(100, activation ="relu"))
model.add(layers.Dense(50, activation ="relu"))
model.add(layers.Dense(10, activation ="softmax"))

model.summary()

# TODO: definiraj karakteristike procesa ucenja pomocu .compile()

model.compile( loss ="categorical_crossentropy", optimizer ="adam", metrics =["accuracy" ,])

batch_size = 32
epochs = 20


# TODO: provedi ucenje mreze
x_train_reshaped = x_train_s.reshape(-1, 784)
#.astype("float32") / 255  
x_test_reshaped = x_test_s.reshape(-1, 784)
#.astype("float32") / 255

history = model.fit( x_train_reshaped , y_train_s , batch_size = batch_size , epochs = epochs , validation_split = 0.1)

predictions = model.predict( x_test_reshaped )
score = model.evaluate( x_test_reshaped , y_test_s , verbose = 0)


# TODO: Prikazi test accuracy i matricu zabune



# TODO: spremi model
model.save ("modelSave.h5")

