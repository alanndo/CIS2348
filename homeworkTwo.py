# 2133915
# Alan Do


import datetime

#find the month number
def findMonths(months):
  if months == "January":
    month = 1
  elif months == "February":
    month = 2
  elif months == "March":
    month = 3
  elif months == "April":
    month = 4
  elif months == "May":
    month = 5
  elif months == "June":
    month = 6
  elif months == "July":
    month = 7
  elif months == "August":
    month = 8
  elif months == "September":
    month = 9
  elif months == "October":
    month = 10
  elif months == "November":
    month = 11
  elif months == "December":
    month = 12
  return month

def findDay(userString):
  #delete the comma from the string sepeartor
  number = userString[1].replace(",","")
  return number

def findYear(year):
  year = userStringOne[2]
  return year


def checkDateFormat(stringss):
  #check if the date given is correct format, if not break 
  return

def findCurrentDate():
  currentDate = datetime.datetime.now()
  
  currentYear = currentDate.year
  currentMonth = currentDate.month
  currentDay = currentDate.day

  return currentMonth, currentDay, currentYear

userString = input()
userStringOne = userString.split(" ") 
#print out the list
print(userStringOne)
#print out the month
print(findMonths(userStringOne[0]))
#print the number date
print(findDay(userStringOne))
#print year
print(findYear(userStringOne))


print(findCurrentDate())






