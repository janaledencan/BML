# Zadatak 2.4.4 Napišite program koji ce kreirati sliku koja sadrži cetiri kvadrata crne odnosno
# bijele boje (vidi primjer slike 2.4 ispod). Za kreiranje ove funkcije koristite numpy funkcije
# zeros i ones kako biste kreirali crna i bijela polja dimenzija 50x50 piksela. Kako biste ih složili
# u odgovarajuci oblik koristite numpy funkcije hstack i vstack.

import numpy as np
import matplotlib.pyplot as plt


zero = np.zeros([50,50], int)
one = np.ones([50,50], int)

first_row = np.hstack((zero,one))
secund_row = np.hstack((one,zero))

image = np.vstack((first_row,secund_row))

plt.imshow(image, cmap="gray")
plt.show()