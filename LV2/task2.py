# Zadatak 2.4.2 Datoteka data.csv sadrži mjerenja visine i mase provedena na muškarcima i
# ženama. Skripta zadatak_2.py ucitava dane podatke u obliku numpy polja data pri cemu je u
# prvom stupcu polja oznaka spola (1 muško, 0 žensko), drugi stupac polja je masa u kg, a treci
# stupac polja je visina u cm.
    # a) Na temelju veliˇcine numpy polja data, na koliko osoba su izvršena mjerenja?
    # b) Prikažite odnos visine i mase osobe pomocu naredbe matplotlib.pyplot.scatter.
    # c) Ponovite prethodni zadatak, ali prikažite mjerenja za svaku pedesetu osobu na slici.
    # d) Izraˇcunajte i ispišite u terminal minimalnu, maksimalnu i srednju vrijednost visine u ovom
    # podatkovnom skupu.
    # e) Ponovite zadatak pod d), ali samo za muškarce, odnosno žene. Npr. kako biste izdvojili
    # muškarce, stvorite polje koje zadrži bool vrijednosti i njega koristite kao indeks retka.
    # ind = (data[:,0] == 1)

import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

# Importing csv module
import csv

with open("data.csv", 'r') as x:
    sample_data = list(csv.reader(x, delimiter=","))

sample_data = np.array(sample_data)
print(sample_data)


#a) 
#print (sample_data.shape) # koliko redaka ima vektor
print(len(sample_data)-1)


# b)
s,height,weight = sample_data.T.tolist()
s=np.delete(s,0)

height=np.delete(height,0) 
weight=np.delete(weight,0) 

h = height.astype(float)
w = weight.astype(float)



# c)
fheight = [h[i] for i in range(len(height)) if i%50==0]
fweight = [w[i] for i in range(len(weight)) if i%50==0]


plt.scatter(fheight, fweight, color = 'g')

plt.xlabel ('Height')
plt.ylabel ('Weight')
plt.title ( 'Scatter plot')

plt.show()


# d)

h = height.astype(float)
print(f"Min height: {min(h)}")
print(f"Max height: {max(h)}")
print(f"Arithmetic value: {mean(h)}")


# e) 

s = s.astype(float)
ind = (s == 1.0) #male
mh = [h[i] for i in range(len(h)) if ind[i]]
fh = [h[i] for i in range(len(h)) if ind[i] == False]

print(f"Min men height: {min(mh)}")
print(f"Max men height: {max(mh)}")
print(f"Arithmetic value men: {mean(mh)}")

print(f"Min women height: {min(fh)}")
print(f"Max women height: {max(fh)}")
print(f"Arithmetic value women: {mean(fh)}")