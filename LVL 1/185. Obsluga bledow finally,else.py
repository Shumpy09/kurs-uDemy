import sys

tasksPerPerson = 0

try:
    tasks = 32
    personStr = input("Podaj liczbe czlonkow zespolu: ")
    persons = int(personStr)

    tasksPerPerson = tasks / persons

except ValueError as e:
    print("Sorry - musisz podac liczbe: ", e)

except ZeroDivisionError as e:
    print("Sorry - musisz podac odpowiednia wartosc wieksza od zera: ",e)

except:
    print("Coś poszło nie tak :/ ", sys.exc_info()[0])

else:
    print("Kazda osoba powinna otrzymac ok. ",tasksPerPerson, " zadan.")

finally:
    print("Script finished with/without errors")