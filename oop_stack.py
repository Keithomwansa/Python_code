# class Stack:
#     def __init__(self):
#         self.__stackList = []
#
#     def push(self, val):
#         self.__stackList.append(val)
#
#     def pop(self):
#         val = self.__stackList[-1]
#         del self.__stackList[-1]
#         print(val, "has been popped")
#         return val # + " has been popped"
#
#
# stackObject = Stack()
#
# stackObject.push(3)
# stackObject.push(2)
# stackObject.push(1)
#
# print(stackObject.pop())
# # print(stackObject.pop())
# print(stackObject.pop())

class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val

littleStack = Stack()
anotherStack = Stack()
funnyStack = Stack()

littleStack.push(1)
anotherStack.push(littleStack.pop() + 1)
funnyStack.push(anotherStack.pop() + 2)

print(funnyStack.pop())