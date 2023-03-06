# Zadatak 2.4.3 Skripta zadatak_3.py ucitava sliku ’road.jpg’. Manipulacijom odgovarajuce
# numpy matrice pokušajte:
# a) posvijetliti sliku, (The alpha blending value, between 0 (transparent) and 1 (opaque).)
# b) prikazati samo drugu cetvrtinu slike po širini,
# c) zarotirati sliku za 90 stupnjeva u smjeru kazaljke na satu,(rotated_img)
# d) zrcaliti sliku.

import numpy as np
import matplotlib . pyplot as plt



img = plt.imread("road.jpg")
img = img [:,:,0].copy()
print(img.shape)
print(img.dtype)
plt.figure()

#a)
plt.imshow(img , cmap ="gray", alpha=0.2)


#b)
rotated_img = np.rot90(img)
plt.imshow(rotated_img)


#c)
height, width= img.shape

start_col = width // 4
end_col = width //2
sliced_img = img[:, start_col:end_col]

plt.imshow(sliced_img)

#Drugi nacin
sliced_img= img[:,110:320]
plt.imshow(sliced_img)


#d)
mirrored_img = np.fliplr(img)

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(img)
ax1.set_title("Original Image")
ax2.imshow(mirrored_img)
ax2.set_title("Mirrored Image")


plt.show()