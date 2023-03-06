
ham=0
spam=0
ham_sms=0
spam_sms=0
usklicnik=0


file = open('SMSSpamCollection.txt', encoding="utf8")
  
  
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
