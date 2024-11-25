def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum

for n in range(1, 10): # testing
    print(n, "->", fib(n))

##
# def fib(n):
# if n < 1:
#         return None
#     if n < 3:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# print(fib(20))

# def factorialFun(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#     return n * factorialFun(n - 1)

# print(factorialFun(20))

# Recursive implementation of the factorial function
def factorial(n):
    if n == 1:    # the base case (termination condition)
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4)) # 4 * 3 * 2 * 1 = 24