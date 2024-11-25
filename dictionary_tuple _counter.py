school_class = {}

while True:
    name = input("Enter the student's name (or type exit to stop): ")
    if name == 'exit':
        break

    score = int(input("Enter the student's score (0-10): "))

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)

for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

##get method
polEngDict = {
    "kwiat" : "flower",
    "woda"  : "water",
    "gleba" : "soil"
    }

item1 = polEngDict["gleba"]    # ex. 1
print(item1)    # outputs: soil

item2 = polEngDict.get("woda")
print(item2)    # outputs: water


#colors
colors = {
    "white" : (255, 255, 255),
    "grey"  : (128, 128, 128),
    "red"   : (255, 0, 0),
    "green" : (0, 128, 0)
    }

for col, rgb in colors.items():
    print(col, ":", rgb)