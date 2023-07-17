# 2133915
# Alan Do


userInt = (input())

List = userInt.split()
List2 = list(map(int, List))

positive_numbers = [num for num in List2 if num >= 0]
positive_numbers.sort()

for i in positive_numbers:
    print(f"{i} ", end="")
        