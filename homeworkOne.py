# Alan Do
# 2133915

print("Birthday Calculator")
currentMonth = int(input())
currentDay = int(input())
currentYear = int(input())
print("Current Day")
print(f"Month: {currentMonth}")
print(f"Day: {currentDay}")
print(f"Year: {currentYear}")
print("Birthday")
birthMonth = int(input())
birthDay = int(input())
birthYear = int(input())
print(f"Month: {birthMonth}")
print(f"Day: {birthDay}")
print(f"Year: {birthYear}")
print(f"You are {currentYear-birthYear} years old.")
if currentMonth == birthMonth and currentDay == birthDay and currentYear == birthYear:
    print("Happy Birthday")
