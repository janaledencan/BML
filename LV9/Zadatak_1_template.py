import numpy as np
from tensorflow import keras
from keras import layers
from keras.datasets import cifar10
from keras.utils import to_categorical
from matplotlib import pyplot as plt
import ssl
import os

ssl._create_default_https_context = ssl._create_unverified_context


# if not os.path.exists('logs/cnn/train'):
#     os.makedirs('logs/cnn/train')



# ucitaj CIFAR-10 podatkovni skup
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# prikazi 9 slika iz skupa za ucenje
plt.figure()
for i in range(9):
    plt.subplot(330 + 1 + i)
    plt.xticks([]),plt.yticks([])
    plt.imshow(X_train[i])

plt.show()


# pripremi podatke (skaliraj ih na raspon [0,1]])
X_train_n = X_train.astype('float32')/ 255.0
X_test_n = X_test.astype('float32')/ 255.0

# 1-od-K kodiranje
y_train = to_categorical(y_train, dtype ="uint8")
y_test = to_categorical(y_test, dtype ="uint8")

# CNN mreza
model = keras.Sequential()
model.add(layers.Input(shape=(32,32,3)))
model.add(layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu', padding='same'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu', padding='same'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Conv2D(filters=128, kernel_size=(3, 3), activation='relu', padding='same'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(500, activation='relu'))
model.add(layers.Dropout(0.3))
model.add(layers.Dense(10, activation='softmax'))

model.summary()

# definiraj listu s funkcijama povratnog poziva
my_callbacks = [
    keras.callbacks.EarlyStopping ( monitor ="val_loss",
        patience = 5,
        verbose = 1),
    
    keras.callbacks.TensorBoard(log_dir = 'logs/batch128',
                                update_freq = 100)
    
]

model.compile(optimizer='adam',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.fit(X_train_n,
            y_train,
            epochs = 20,
            batch_size = 128,
            callbacks = my_callbacks,
            validation_split = 0.1)


score = model.evaluate(X_test_n, y_test, verbose=0)
print(f'Tocnost na testnom skupu podataka: {100.0*score[1]:.2f}')

# 1.zad
# Od kojih se slojeva sastoji CNN mreža? 3 konvolucijska sloja, 3 sloja sažimanja po maksimalnoj vrijednosti, sloj ravnanja i 2 potpuno povezana sloja, naknadno je dodan droput sloj
# Koliko ima parametara mreža? 1,122,758
#tocnost klasifikacije i prosjecnu vrijednost funkcije gubitka
#na skupu podataka za ucenje i skupu podataka za validaciju. Što se dogodilo tijekom ucenja
#mreže? 


#tocnost klasifikacije na trening skupu = 0.9858
#tocnost klasifikacije na validacijskom skupu = 0.7433


# 2.zad
#Kako komentirate utjecaj dropout slojeva na performanse mreže?

#tocnost klasifikacije na trening skupu = 0.9736
#tocnost klasifikacije na validacijskom skupu = 0.7631
#Dodavanjem dropout sloja smanjila se tocnost na skupu za treniranje, a povecala pri validaciji


# 3.zad
#Kod funkcije povratnog poziva za rano zaustavljanje koja zaustavi proces
#ucenja nakon što se 5 uzastopnih epoha ne smanji prosjecna vrijednost funkcije gubitka na
#validacijskom skupu:

#tocnost klasifikacije na trening skupu = 0.891
#tocnost klasifikacije na validacijskom skupu = 0.7616

# smanjila se tocnost na train skupu, a vrijednost na validation skupu je veca od pocetne, a malo manja od proslog samo s dropout slojem
# za ovaj zadatak zaustavljanje se odgodilo na 12 epohi   

# 4.zad
# Što se dogada s procesom ucenja:
# 1. ako se koristi jako velika ili jako mala velicina serije?
#    Kada se batch size postavi na 32 zaustavljanje se dogodi na 11. epohi(uzme 32 podatka u 1407 iteracija), a pri batch size-u 128 zaustavljanje se dogodi na 14. epohi (uzme 128 podatka u 352 iteracija epohe)
#    Tocnost je na trening skupu za BS 32 = 0.8844 dok je kod BS 128 = 0.8998, kod validacijskog skupa BS 32 = 0.7582, a BS 128 = 0.7638
# 2. ako koristite jako malu ili jako veliku vrijednost stope ucenja?
#    Ako je velika brze ce uciti, ali nece doci do minimuma
# 3. ako izbacite odredene slojeve iz mreže kako biste dobili manju mrežu?
#    Epohe se brze izvode i manja je tocnost.
# 4. ako za 50% smanjite velicinu skupa za ucenje?
#    Manje je podataka u svakoj epohi, brze se izvode te je manja tocnost.


