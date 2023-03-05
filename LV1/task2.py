# Zadatak 1.4.2 Napišite program koji od korisnika zahtijeva upis jednog broja koji predstavlja
# nekakvu ocjenu i nalazi se izmedu 0.0 i 1.0. Ispišite kojoj kategoriji pripada ocjena na temelju
# sljedecih uvjeta:
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# Ako korisnik nije utipkao broj, ispišite na ekran poruku o grešci (koristite try i except naredbe).
# Takoder, ako je broj izvan intervala [0.0 i 1.0] potrebno je ispisati odgovarajuc´u poruku.

try:
    grade=input("Enter number whick represents grade (0.0 - 1.0): ")

    if (grade >= '0.9') and (grade <= '1.0'):
        print('A')
    elif grade >= '0.8' and (grade <= '1.0'):
        print('B')
    elif grade >= '0.7' and (grade <= '1.0'):
        print('C')
    elif grade >= '0.6' and (grade <= '1.0'):
        print('D')
    elif grade < '0.6' and (grade <= '1.0'):
        print('F')
    elif (grade < '0.0') or (grade > '1.0'):
        print("Number is not valid.")

except:
    print("You have not entered any number")