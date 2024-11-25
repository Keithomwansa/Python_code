dictionary = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
phone_numbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

print(dictionary['cat'])
print(phone_numbers['Suzy'])

words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")


dictionary = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])
    print(key)
for english, french in dictionary.items():
    print(english, "->", french)
for french in dictionary.values():
    print(french)
## dd value to a dictionary

dictionary.update({"duck" : "canard"})
print(dictionary)
dictionary['swan'] = 'cygne'
print(dictionary)

##delete key from a dictionary
del dictionary['dog']
print(dictionary)

#pop an item from a dictionary
dictionary.popitem()
print(dictionary)


