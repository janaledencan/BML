# Zadatak 3.4.1 Skripta zadatak_1.py ucitava podatkovni skup iz data_C02_emission.csv.
# Dodajte programski kod u skriptu pomocu kojeg možete odgovoriti na sljedeca pitanja:

# a) Koliko mjerenja sadrži DataFrame? Kojeg je tipa svaka velicina? Postoje li izostale ili
# duplicirane vrijednosti? Obrišite ih ako postoje. Kategoricke velicine konvertirajte u tip
# category.

import pandas as pd
data = pd. read_csv ( 'data_C02_emission.csv')
data.info()
print(f"There is:{data.duplicated().sum()} duplicated values")
data.drop_duplicates()

# print(f'Dataframe has: {len(data)} entries')
# print(data.dtypes)
# print(data.isna().sum())
# print(data.duplicated().sum())
# data.dropna()
# data.drop_duplicates()




# b) Koja tri automobila ima najvecu odnosno najmanju gradsku potrošnju? Ispišite u terminal:
# ime proizvodaca, model vozila i kolika je gradska potrošnja.

# c) Koliko vozila ima velicinu motora izmedu 2.5 i 3.5 L? Kolika je prosjecna C02 emisija
# plinova za ova vozila?

# d) Koliko mjerenja se odnosi na vozila proizvodaca Audi? Kolika je prosjecna emisija C02
# plinova automobila proizvodaca Audi koji imaju 4 cilindara?

# e) Koliko je vozila s 4,6,8. . . cilindara? Kolika je prosjecna emisija C02 plinova s obzirom na
# broj cilindara?

# f) Kolika je prosjecna gradska potrošnja u slucaju vozila koja koriste dizel, a kolika za vozila
# koja koriste regularni benzin? Koliko iznose medijalne vrijednosti?

# g) Koje vozilo s 4 cilindra koje koristi dizelski motor ima najvecu gradsku potrošnju goriva?

# h) Koliko ima vozila ima rucni tip mjenjaca (bez obzira na broj brzina)?

# i) Izracunajte korelaciju izmedu numerickih velicina. Komentirajte dobiveni rezultat.