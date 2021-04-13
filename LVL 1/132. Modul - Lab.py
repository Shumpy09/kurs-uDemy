import math

inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]
'''
print(len(inputdata))
print(len(factortable))

if len(inputdata) == len(factortable):
    print("OK")        
    i = 0
    while i<len(inputdata):
        minvalue = inputdata[i] - factortable[i] * inputdata[i]
        maxvalue = inputdata[i] + factortable[i] * inputdata[i]
        print("Minvalue: ", minvalue, "Maxvalue: ", maxvalue)

        mininteger = math.floor(minvalue)
        maxinteger = math.ceil(maxvalue)
        print("Miniteger: ", mininteger, "Inputdata: ", inputdata[i], "Maxinteger: ", maxinteger)

        i += 1

else:
    print("Inputdata and factorable need to have equal number of elements")
'''

import random
'''
i = 0
while i < len(inputdata):
    minvalue = inputdata[i] - random.random() * inputdata[i]
    maxvalue = inputdata[i] + random.random() * inputdata[i]
    mininteger = math.floor(minvalue)
    maxinteger = math.ceil(maxvalue)

    print("Minvalue: ", minvalue, "Maxvalue: ", maxvalue)
    print("Mininteger: ", mininteger, "Maxinteger: ", maxinteger)
    i += 1
'''

import datetime

print(datetime.datetime.today())
print(datetime.datetime.today().strftime("%Y-%m-%d"))


