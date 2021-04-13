myvar = "Hello VIsual Studio Code!"
myvar2 = myvar+'!!'
print(myvar,myvar2)
print(type(myvar), type(myvar2))
print("Is valute the same?", myvar == myvar2)
print("Are the variable the same?", myvar is myvar2)
print(id(myvar), id(myvar2))

myvar2 = myvar2[:-2]
print(myvar,myvar2)
print(type(myvar), type(myvar2))
print("Is valute the same?", myvar == myvar2)
print("Are the variable the same?", myvar is myvar2)
print(id(myvar), id(myvar2))