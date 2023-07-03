# 2133915
# Alan Do




def palindrome(user_val):

    li = list(delWhitespace)
    reversedLi = list(reversed(li))

    if li == reversedLi:
        print(f"{userInt} is a palindrome")
    else:
        print(f"{userInt} is not a palindrome")

userInt = input()
delWhitespace = userInt.replace(" ","")
palindrome(delWhitespace)