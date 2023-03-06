# br_radnih_sati = input("Unesite broj radnih sati: ")
# cijena_po_satu = input("Unesite cijenu svoga rada po satu: ")
# zarada = float(br_radnih_sati) * float(cijena_po_satu)

# print(zarada)


sati=input("Unesite broj radnih sati: ")
cijena_po_satu = input("Unesite cijenu svoga rada po satu: ")

def total_euro(hours, price):
    print(float(hours)*float(price))

total_euro(sati, cijena_po_satu)

