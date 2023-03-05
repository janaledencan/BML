# Zadatak 1.4.4 Napišite Python skriptu koja ce ucitati tekstualnu datoteku naziva song.txt.
            # Potrebno je napraviti rjecnik koji kao kljuceve koristi sve razlicite rijeci koje se pojavljuju u
            # datoteci, dok su vrijednosti jednake broju puta koliko se svaka rijec (kljuc) pojavljuje u datoteci.
            # Koliko je rijeci koje se pojavljuju samo jednom u datoteci? Ispišite ih.

file = open ('song.txt')
my_dictionary={}  #key:value
counter=0
i=0

for line in file:
    for word in line.split():  #rastavi svaku rijec
        if word in my_dictionary.keys():
           value=my_dictionary.get(word)
           my_dictionary.update({f"{word}":value+1})
        else:
            my_dictionary.update({f"{word}":1})


for value in my_dictionary.values():
    if value == 1:
        counter+=1


print(counter)
for item in my_dictionary.items():
    print(item)
    
file.close ()
