# 2133915
# Alan Do


#equation one ax + bx = c
eqA = int(input())
eqB = int(input())
eqC = int(input())
#equation two dx + de = f
eqD = int(input())
eqE = int(input())
eqF = int(input())




boolean = False
for x in range(-10,10):
    for y in range(-10,10):
        if (eqA*x) + (eqB*y) == eqC and (eqD*x) + (eqE*y) == eqF:
            boolean = True            
            print(x,y)
if boolean == False:
    print("No solution")



         

