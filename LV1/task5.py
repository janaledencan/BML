# Zadatak 1.4.5 Napišite Python skriptu koja ce ucitati tekstualnu datoteku naziva SMSSpamCollection.txt
        # [1]. Ova datoteka sadrži 5574 SMS poruka pri cemu su neke oznacene kao spam, a neke kao ham.
        # Primjer dijela datoteke:
        # ham Yup next stop.
        # ham Ok lar... Joking wif u oni...
        # spam Did you hear about the new "Divorce Barbie"? It comes with all of Ken’s stuff!
        # a) Izracunajte koliki je prosjecan broj rijeci u SMS porukama koje su tipa ham, a koliko je
        # prosjecan broj rijeci u porukama koje su tipa spam.
        # b) Koliko SMS poruka koje su tipa spam završava usklicnikom ?



ham=0
spam=0
ham_sms=0
spam_sms=0
usklicnik=0


file = open('SMSSpamCollection.txt', encoding="utf8")
  
# reading each line   
for line in file:
    words=line.split()      

    if words[0] == "ham":
        ham+=len(words) #br. rijeci
        ham_sms+=1 #br. recenica
    else:
        spam+=len(words)
        spam_sms+=1
        #usklicnik
        if words[len(words)-1]=='!':
            usklicnik+=1
                
file.close ()

print(f"Avg Ham: {ham/ham_sms}")
print(f"Avg Spam: {spam/spam_sms}")
print(usklicnik)
