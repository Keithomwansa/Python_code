from random import randint

for i in range(10):
    print(randint(1, 10), end=',')

from random import choice, sample

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(lst))
print(sample(lst, 5))
print(sample(lst, 10))

from platform import platform
#
# print(platform())
# print(platform(1))
# print(platform(0, 1))