def isYearLeap(year):
#
# your code from LAB 4.1.3.6
    if year % 4 == 0:
        return True
    else:
        return False

def daysInMonth(year, month):
    if year % 4 == 0 and month == 2:
        return 29
    else:
        return 28
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 \
            or month == 10 or month == 12:
        return 31
    else:
        return 30
# put your new code here
#

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")