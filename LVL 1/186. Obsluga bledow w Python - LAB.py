import os

line = input("Jaka jest cena kursu: ")
path = input("Podaj ścieżkę do pliku: ")

try:
    file = open(path, 'w')
    file.write(line)
    file.close()
    value = int(line)
    print("The value saved in file is: ", value)    

except FileNotFoundError as e:
    print("Eror opening file: ", path, e)

except ValueError as e:
    print("The value entered cannot be converted to a number: ", e)

except:
    print("SORRY, MAMY PROBLEM")

else:
    print("Actions completed successfully")

