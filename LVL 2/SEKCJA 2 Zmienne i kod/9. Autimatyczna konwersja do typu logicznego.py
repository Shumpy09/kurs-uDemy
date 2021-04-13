# napis niepusty zawsze jest prawdą

isOK = 'True'       # isOK = ''
print("Variable isOK: ", isOK, type(isOK))
if isOK:
    print('TRUE')

isOK = ''
print("Variable isOK: ", isOK, type(isOK))
if isOK:
    print('TRUE')

isOK = 1
print("Variable isOK: ", isOK, type(isOK))
if isOK:
    print('TRUE')

isOK = 0
print("Variable isOK: ", isOK, type(isOK))
if isOK:
    print('TRUE')

isOK = -1
print("Variable isOK: ", isOK, type(isOK))
if isOK:
    print('TRUE')

isOK = [1,2,3]
print("Variable isOK: ", isOK, type(isOK))
if isOK:
    print('TRUE')

isOK = []
print("Variable isOK: ", isOK, type(isOK))
if isOK:
    print('TRUE')

isOK = [0,0,0]
print("Variable isOK: ", isOK, type(isOK))
if isOK:
    print('TRUE')

isOK = [0,0,0]
print("Variable isOK: ", isOK, type(isOK))
if isOK[0]:             # odwołanie się do 0 elementu listy
    print('TRUE')

listOfErrors = [100,101,102]
print("Variable listOfErrors: ", listOfErrors, type(listOfErrors))
if len(listOfErrors) > 0:
    print('TRUE')
