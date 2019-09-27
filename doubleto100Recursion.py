#Doubleto100 Recursion

def doubleto100(num):
	if num > 100:
		return 0
		
	return doubleto100(2 * num) + 1
print(doubleto100(10))