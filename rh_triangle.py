def isItATriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


a = float(input("Enter the first side's length: "))
b = float(input("Enter the second side's length: "))
c = float(input("Enter the third side's length: "))

if isItATriangle(a, b, c):
    print("Congratulations - it can be a triangle.")
else:
    print("Sorry, it won't be a triangle.")


def isItRightTriangle(a, b, c):
    if not isItATriangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2


print(isItRightTriangle(a, b, c))
print(isItRightTriangle(a, b, c))