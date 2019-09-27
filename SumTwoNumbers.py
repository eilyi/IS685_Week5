#sum two numbers and print

import sys
if len(sys.arg) !=3:
    print("Blaj blah" + sys.argv[0] + " <first number> <second number>)
    sys.exit()
   first= sys.argv[1]
   second = sys.argv[2]
   
   print("{0} and {1}".format(first,second))
   
   result= first + second
   print(result)