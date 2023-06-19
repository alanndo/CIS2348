# Alan Do
# 2133915

height = int(input())
width = int(input())
color = input()

area = (height * width)

paint = 1/350
paintNeeded = area*paint
paintRounded= round(paintNeeded)

print("Enter wall height (feet):")
print("Enter wall width (feet):")
print(f"Wall area: {area} square feet")
print(f"Paint needed: {paintNeeded:.2f} gallons".format((area/paint)))
print(f"Cans needed: {paintRounded} can(s)")
print()
print(f"Choose a color to paint the wall:")

if color == "red":
    print(f"Cost of purchasing red paint: ${paintRounded*35}")
elif color == "blue":
    print(f"Cost of purchasing blue paint: ${paintRounded*25}")
elif color == "green":
    print(f"Cost of purchasing green paint: ${paintRounded * 23}")
