def PrintAnimal(*animals):

    cat = "To jest kot"
    bat = "To jest nietoperz"
    bear = "To jest niedźwiedź"

    for animal in animals:

        if animal == 'bat':
            print(bat)
        elif animal == 'cat':
            print(cat)
        elif animal == 'bear':
            print(bear)
        else:
            print("Cannot print '%s'. Correct values for the parameter are: cat, bat, bear." % animal)
        
    return
'''   
if PrintAnimal():
    print("The parameter was correct")
else:
    print("The parameter was INCORRECT")

if PrintAnimal('dog'):
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')

if PrintAnimal('bat'):
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')
'''

PrintAnimal('bat')
print("=========")
PrintAnimal('cat', 'bat')
print("=========")
PrintAnimal('cat', 'bat', 'bear', 'dog', 'bear', 'bat')
print("--------")
PrintAnimal()
print("=========")