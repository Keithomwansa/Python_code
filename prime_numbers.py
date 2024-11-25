def isPrime(num):
#
# put your code here
    if num == 2:
        return True
    else:
        i = 2
        while i < num:
            if num%i == 0:
                return False
                break
            else:
                i += 1
        else:
            return True
for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()
