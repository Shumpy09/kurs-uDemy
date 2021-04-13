import os

filename = input("Podaj ścieżkę do pliku a zadresami: ")

while not os.path.isfile(filename):
    print("Błędna ścieżka, spróbuj ponownie")
    filename = input("Podaj ścieżkę do pliku z adresami: ")

webaddresses = []

with open(filename,'r') as file:

    for line in file:
        webaddresses.append(line.replace("\n",''))

for line in webaddresses:

    if line.endswith(".pl"):
        print("adres %s jest adresem z Polski" % line)
        
    else:
        print("adres %s nie jest adresem z Polski" % line)