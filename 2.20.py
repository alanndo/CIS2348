# Alan Do
# 2133915

lemon = int(input())
water = int(input())
agave = float(input())
servings = int(input())
print("Enter amount of lemon juice (in cups):")
print("Enter amount of water (in cups):")
print("Enter amount of agave nectar (in cups):")
print("How many servings does this make?")
print()
print(f"Lemonade ingredients - yields {servings:.2f} servings".format(servings))
print(f"{lemon:.2f} cup(s) lemon juice".format(lemon))
print(f"{water:.2f} cup(s) water".format(water))
print(f"{agave:.2f} cup(s) agave nectar".format(agave))
print()
desiredServings = int(input())
lemonGallon = (desiredServings/3)/16
waterGallon = (desiredServings*2.66666666667)/16
agaveGallon = (desiredServings/2.4)/16
print("How many servings would you like to make?")
print()
print(f"Lemonade ingredients - yields {desiredServings:.2f} servings".format(desiredServings))
print(f"{(desiredServings/3):.2f} cup(s) lemon juice".format((desiredServings/3)))
print(f"{(desiredServings*2.66666666667):.2f} cup(s) water".format((desiredServings*2)))
print(f"{(desiredServings/2.4):.2f} cup(s) agave nectar".format((desiredServings/2.4)))
print()
print(f"Lemonade ingredients - yields {desiredServings:.2f} servings".format(desiredServings))
print(f"{lemonGallon:.2f} gallon(s) lemon juice".format(lemonGallon))
print(f"{waterGallon:.2f} gallon(s) water".format(waterGallon))
print(f"{agaveGallon:.2f} gallon(s) agave nectar".format(agaveGallon))


