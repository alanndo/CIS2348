# 2133915
# Alan Do

import csv

userInt = input()
# open the file
with open(userInt, "r")as f:
  words = csv.reader(f)
  
  for row in words:
    listWords = row


unlist = list(dict.fromkeys(listWords))
for i in range(len(unlist)):
  print(unlist[i],listWords.count(unlist[i]))
    
