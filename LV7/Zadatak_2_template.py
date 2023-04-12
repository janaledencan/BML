import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as Image
from sklearn.cluster import KMeans

from sklearn.cluster import KMeans
import numpy as np


# ucitaj sliku
img = Image.imread("imgs\\test_1.jpg")

# prikazi originalnu sliku
plt.figure()
plt.title("Originalna slika")
plt.imshow(img)
plt.tight_layout()
# plt.show()

# pretvori vrijednosti elemenata slike u raspon 0 do 1
img = img.astype(np.float64) / 255

# transfromiraj sliku u 2D numpy polje (jedan red su RGB komponente elementa slike)
w,h,d = img.shape
img_array = np.reshape(img, (w*h, d))

print(img_array)  #matrica RGB
print(img_array.shape)

# rezultatna slika
img_array_aprox = img_array.copy()



# inicijalizacija algoritma K srednjih vrijednosti
km = KMeans( n_clusters = 5, init ='random', n_init = 5, random_state = 0)

# pokretanje grupiranja primjera
km.fit(img_array_aprox)

# dodijeljivanje grupe svakom primjeru
labels = km.predict(img_array_aprox)



print(km.cluster_centers_) #ispis vrijednosti centara

#rgb_cols = km.cluster_centers_.round(0).astype(int) #promijena vrijednosti centara u RGB int vriejdnosti
#print(rgb_cols)

img_quant = np.reshape(km.cluster_centers_[labels],(h,w,-1)) #Assign all cluster points to the cluster center (a u reshapeu je bio rgb_cols treci prametar je bio d)

plt.imshow(img_quant) #Display the color quantized image
#plt.tight_layout()

# fig, ax = plt.subplots(1,2, figsize=(w,h))
# ax[0].imshow(img_array_aprox)
# ax[0].set_title('Original Image')
# ax[1].imshow(img_quant)
# ax[1].set_title('Color Quantized Image')

plt.show()

