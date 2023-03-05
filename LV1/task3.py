# Zadatak 1.4.3 Napišite program koji od korisnika zahtijeva unos brojeva u beskonacnoj petlji
            # sve dok korisnik ne upiše „Done“ (bez navodnika). Pri tome brojeve spremajte u listu. Nakon toga
            # potrebno je ispisati koliko brojeva je korisnik unio, njihovu srednju, minimalnu i maksimalnu
            # vrijednost. Sortirajte listu i ispišite je na ekran. Dodatno: osigurajte program od pogrešnog unosa
            # (npr. slovo umjesto brojke) na nacin da program zanemari taj unos i ispiše odgovarajucu poruku.


def average_value(lst):
    return sum(lst) / len(lst)


my_list=[]
counter=0
my_input="initial"

while(my_input != "Done"):
   
    my_input=input("Enter number: ")
    if ((my_input >= 'A' and my_input <= 'Z') or (my_input >= 'a' and my_input <= 'z')) and my_input!="Done":  #without letters
        print("Invalid input, not counting")
    elif my_input != "Done":  #all num
        my_list.append(float(my_input))
        counter+=1


print(f"You have entered {counter} numbers")

average = average_value(my_list)
min_value=min(my_list)
max_value=max(my_list)
my_list.sort()

print("Average of the list =", round(average, 2))
print(f"Min value: {min_value} and max value: {max_value}")
print(my_list)

