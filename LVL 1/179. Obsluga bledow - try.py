import sys

tasksPerPerson = 0

try:
    tasks = 32
    personStr = input("Podaj liczbe czlonkow zespolu: ")
    persons = int(personStr)

    tasksPerPerson = tasks / persons

except:
    print("Coś poszło nie tak :/ ", sys.exc_info()[0])

print("Kazda osoba powinna otrzymac ok. ",tasksPerPerson, " zadan.")
