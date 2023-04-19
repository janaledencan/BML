import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
import numpy as np

#1. Upoznajte se s ucitanim podacima. Koliko primjera sadrži skup za ucenje, a koliko skup za
#testiranje? Kako su skalirani ulazni podaci tj. slike? Kako je kodirana izlazne velicina?

mnist = tf.keras.datasets.mnist  #28x28 images of hand-written digits 0-9

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# x_train = tf.keras.utils.normalize(x_train, axis=1)
# x_test = tf.keras.utils.normalize(x_test, axis=1)


#2. Pomocu matplotlib biblioteke prikažite jednu sliku iz skupa podataka za ucenje te ispišite
#njezinu oznaku u terminal.

plt.imshow(x_train[0], cmap=plt.cm.binary)
plt.show()
#print(x_train[0])

#3. Pomocu klase Sequential izgradite mrežu prikazanu na slici 8.5. Pomocu metode
#.summary ispišite informacije o mreži u terminal.

model = tf.keras.models.Sequential() 
model.add (tf.keras.layers.Input( shape =(784, )))
model.add(tf.keras.layers.Dense(100, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(50, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model.summary()
#4. Pomocu metode .compile podesite proces treniranja mreže.
#5. Pokrenite ucenje mreže (samostalno definirajte broj epoha i velicinu serije). Pratite tijek
#ucenja u terminalu.

x_train_reshaped = x_train.reshape(-1, 784).astype("float32") / 255  #DODAJ GORE ODREDIVANJE BROJA EL. 60000 i 10000
x_test_reshaped = x_test.reshape(-1, 784).astype("float32") / 255

oh_encoder=OneHotEncoder()
y_train_encoded = oh_encoder.fit_transform(np.reshape(y_train,(-1,1))).toarray() #OHE treba 2d array, pa se koristi reshape (-1,1), tj (n,1),
y_test_encoded = oh_encoder.transform(np.reshape(y_test,(-1,1))).toarray() #-1 oznacava da sam otkrije koliko, mora toarray()

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train_reshaped, y_train_encoded, epochs=3, batch_size = 25)

#6. Izvršite evaluaciju mreže na testnom skupu podataka pomocu metode .evaluate.

val_loss, val_acc= model.evaluate(x_test_reshaped, y_test_encoded)
print(val_loss, val_acc)

#7. Izracunajte predikciju mreže za skup podataka za testiranje. Pomocu scikit-learn biblioteke
#prikažite matricu zabune za skup podataka za testiranje.

predictions=model.predict([x_test_reshaped])
predict_num=np.argmax(predictions, axis=1)
print(predict_num)

#8. Pohranite model na tvrdi disk.
model.save('reader/') 


#GOOGLATI ...KAO DA NESTO NEMAM SKINUTO PA SE NE SEJVA











