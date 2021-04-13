def PrintAnimal(animal):

    cat = "To jest kot"
    bat = "To jest nietoperz"
    bear = "To jest niedźwiedź"

    if animal == 'bat':
        print(bat)
    elif animal == 'cat':
        print(cat)
    elif animal == 'bear':
        print(bear)
    else:
        print("Cannot print '%s'. Correct values for the parameter are: cat, bat, bear." % animal)

    return

PrintAnimal('cat')
PrintAnimal(animal = 'bear')
PrintAnimal('bat')
PrintAnimal('dog')
