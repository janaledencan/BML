
file = open ('song.txt')
my_dictionary={}  #key:value
counter=0
i=0

for line in file:
    for word in line.split():  
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
