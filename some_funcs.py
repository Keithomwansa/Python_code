def intro(a, b="Bond"):
    print("My name is", b + ".", a + ".")

intro("Susan")

def boring_function():
    print("'Boredom Mode' ON.")
    return 123

print("This lesson is interesting!")
boring_function()
print("This lesson is boring...")


def strangeFunction(n):
    if (n % 2 == 0):
        return True
    else:
        return False


print(strangeFunction(2))
print(strangeFunction(1))
print(strangeFunction(5))
print(strangeFunction(11))

##
def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s


print(list_sum([5, 4, 3]))

##
def strangeListFunction(n):
    strangeList = []

    for i in range(0, n):
        strangeList.insert(0, i)

    return strangeList


print(strangeListFunction(5))


#parametrized functions
#function to test if yesr is leap year
def isYearLeap(year):
#
    if year % 4 == 0:
        return True
    else:
        return False
#

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
