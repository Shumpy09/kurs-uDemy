def DisplayOptions(options):
    for i in range(len(options)):
        print("{} - {}".format(i+1, options[i]))

    choice = input('Wybierz jedna z opcji: ')
    return choice

options = ['load data', 'export data', 'analyze & predict']
choice = 'x'

while choice:
    choice = DisplayOptions(options)

    if choice:
        try:
            choice_num = int(choice)-1
            if choice_num >= 0 and choice_num < len(options):
                print('Zostala wybrana opcja {} - {} '.format(choice_num+1,options[choice_num]))
            else:
                print('Wartosc jest nieprawidlowa')
        except:
            print('Nieprawdilowa wartosc. Musi zostac wprowadzona liczba')
    else:
        print("Program finished")

