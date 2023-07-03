#2133915
#Alan Do


def changePassword():
  password = input()

  password = password.replace("i","!")
  password = password.replace("a","@")
  password = password.replace("m","M")
  password = password.replace("B","8")
  password = password.replace("o",".")
  password = password + "q*s"

  return password

print(changePassword()) 