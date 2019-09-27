#def DoubleTo100

def DoubleTo100(value):
	#Return how many times the input is double to exceed 100 
	#Need while loop
	doubledValue= value
	n = 0						#Set to zero outside of the loop
	while doubledValue <=100:
		#do something
		n +=1 					#counts inside the loop
		doubledValue = doubledValue * 2
		
	return value

print( "n".format(DoubleTo100(10)))