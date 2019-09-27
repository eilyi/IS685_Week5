#multiply these
num1= 1
num2 = 2

def MultiplyThese(num1, num2):
	print(num1)
    print(num2)
	multiply = num1*num2
	return MultiplyThese(multiply)