import random
'''
min = 1
max = 6

dice = random.randint(min,max)
print(dice)

if dice == 1:
    print("   ","   ","   ")
    print("   "," o ","   ")
    print("   ","   ","   ")
   
elif dice == 2:
    print("   ","  ","  o")
    print("   ","  ","   ")
    print(" o ","  ","   ")
 
elif dice == 3:
    print("   ","  "," o")
    print("   "," o ","  ")
    print(" o ","  ","   ")
 
elif dice == 4:
    print(" o  "," ","o")
    print("   ","  "," ")
    print(" o ","  ","o")

elif dice == 5:
    print(" o "," ","o")
    print("  "," o "," ")
    print(" o "," ","o")
 
elif dice == 6:
    print(" o "," ","o")
    print(" o "," ","o")
    print(" o "," ","o")
'''

dices = []
min = 1
max = 6

for i in range(5):
    #dices.append(random.randint(min,max))
    dice = random.randint(min,max)
    dices.append(dice)
    print(dices)
dices.sort()
print(dices)



