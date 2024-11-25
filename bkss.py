ls = [[c for c in range(r)] for r in range(3)]
for x in ls:
    if len(x)< 2:
        print(4)

# class A:
#
#     def __init__(self, v):
#         self.a = v + 1
# a = A(0)
# print(a._a)

class A:
    A = 1
    def __init__(self, v=2):
        self.v = v + A.A
        A.A +=1

    def set(self, v):
        self.v += v
        A.A += 1
        return
a = A()
a.set(2)
print(a.v)
