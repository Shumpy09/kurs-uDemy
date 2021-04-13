import os

filename = input("Podaj ścieżkę do pliku a zadresami: ")

while not os.path.isfile(filename):
    print("Błędna ścieżka, spróbuj ponownie")
    filename = input("Podaj ścieżkę do pliku z adresami: ")

webaddresses = []

with open(filename,'r') as file:

    for line in file:
        webaddresses.append(line.replace("\n",''))

dirname = os.path.dirname(filename)
websPathPl = os.path.join(dirname,"webs_pl.txt")
websPathOther = os.path.join(dirname,"webs_other.txt")

filePl = open(websPathPl,"w")
fileOther = open(websPathOther,"w")

for line in webaddresses:
    if line.endswith('.pl'):
        filePl.write(line+"\n")
        
    else:
        fileOther.write(line+"\n")
filePl.close()
fileOther.close()

