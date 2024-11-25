def fun(n):
    for i in range(n):
        yield i


for v in fun(5):
    print(v)


##better func
def powersOf2(n):
    pow = 1
    for i in range(n):
        yield pow
        pow *= 2

for v in powersOf2(8):
    print(v)