# Alan Do
# 2133915

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")



userInt = input()
userIntTwo = input()
dollarAmountOne = 0
dollarAmountTwo = 0
if userInt == "Oil change":
    dollarAmountOne = 35
elif userInt == "Tire rotation":
    dollarAmountOne = 19
elif userInt == "Car wash":
    dollarAmountOne = 7
elif userInt == "Car wax":
    dollarAmountOne = 12
elif userInt == "-":
    userInt = "No service"

if userIntTwo == "Oil change":
    dollarAmountTwo = 35
elif userIntTwo == "Tire rotation":
    dollarAmountTwo = 19
elif userIntTwo == "Car wash":
    dollarAmountTwo = 7
elif userIntTwo == "Car wax":
    dollarAmountTwo = 12
elif userIntTwo == "-":
    userIntTwo = "No service"



total = dollarAmountOne + dollarAmountTwo
print()
print("Select first service:")
print("Select second service:")
print()
print("Davy's auto shop invoice")
print()
print(f"Service 1: {userInt}, ${dollarAmountOne}")
print(f"Service 2: {userIntTwo}, ${dollarAmountTwo}")
print()
print(f"Total: ${total}")

