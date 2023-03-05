# Zadatak 1.4.1 Napišite program koji od korisnika zahtijeva unos radnih sati te koliko je placen
                # po radnom satu. Koristite ugradenu Python metodu input(). Nakon toga izracunajte koliko
                # je korisnik zaradio i ispišite na ekran. Na kraju prepravite rješenje na nacin da ukupni iznos
                # izracunavate u zasebnoj funkciji naziva total_euro.
    # Primjer:
    # Radni sati: 35 h
    # eura/h: 8.5
    # Ukupno: 297.5 eura

# br_radnih_sati = input("Unesite broj radnih sati: ")
# cijena_po_satu = input("Unesite cijenu svoga rada po satu: ")
# zarada = float(br_radnih_sati) * float(cijena_po_satu)

# print(zarada)


sati=input("Unesite broj radnih sati: ")
cijena_po_satu = input("Unesite cijenu svoga rada po satu: ")

def total_euro(hours, price):
    print(float(hours)*float(price))

total_euro(sati, cijena_po_satu)

