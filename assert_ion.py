import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)


# the code shows an extravagant way
# of leaving the loop

list = [31, 2, 3, 4, 5]
ix = 0
doit = True

while doit:
    try:
        print(list[ix])
        ix += 1
    except IndexError:
        doit = False

print('Done')