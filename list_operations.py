numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers) # printing original list content

numbers[0] = 111
print("\nPrevious list content:", numbers) # printing previous list content

numbers[1] = numbers[4] # copying value of the fifth element to the second
print("Previous list content:", numbers) # printing previous list content

print("\nList's length:", len(numbers)) # printing previous list length

###
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#
del numbers[1] # removing the second element from the list
print("New list's length:", len(numbers)) # printing new list length
print("\nNew list content:", numbers) # printing current list content

###
myList = [10, 8, 6, 4, 2]
newList = myList[:]
print(newList)


myList = [10, 8, 6, 4, 2]
del myList[1:3]


##
myList = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = myList[0]

for i in myList:
    if i > largest:
        largest = i

print(largest)
