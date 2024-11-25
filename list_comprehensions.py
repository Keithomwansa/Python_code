lst = []

for x in range(10):
    lst.append(1 if x % 2 == 0 else 0)

print(lst)

##
listOne = []

for ex in range(6):
    listOne.append(10 ** ex)


listTwo = [10 ** ex for ex in range(6)]

print(listOne)
print(listTwo)

#
lst = [1 if x % 2 == 0 else 0 for x in range(10)]

print(lst)

genr = (1 if x % 2 == 0 else 0 for x in range(10))

for v in lst:
    print(v, end=" ")
print()

for v in genr:
    print(v, end=" ")
print()

#It's the parentheses. The brackets make a comprehension,
#the parentheses make a generator.
#alternative shown below

for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end=" ")
print()

for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end=" ")
print()

#
