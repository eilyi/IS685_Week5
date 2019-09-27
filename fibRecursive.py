#def fibRecursive(n):

def fibRecursive(n):
	#fib_n = fib_n-1 + fib_n-2
	if n== 0 :
		return 0
	if n== 1:
		return 1
	return fibRecursive(n-1) + fibRecursive(n-2)
print(fibRecursive(9))