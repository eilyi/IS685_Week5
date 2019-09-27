#subtractRecursion

def subtractto10(num):
        #check if at base case
    if num==10:
        return 0
    return subtractto10(num-1) + 1
    
  print("Number of recursions : {0}".format(subtractto10(20)))