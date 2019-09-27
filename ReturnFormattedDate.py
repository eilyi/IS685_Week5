#Return formatted date of 3 days before now (no arguments)

from datetime import date, timedelta

def formatDate3Days():
   3Days = date.today() + timedelta(days=3)
   return 3Days
   
   
 thedate = formatDate3Days()
 print(thedate)
    