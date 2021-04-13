import os

webaddresses = []
line = input("Podaj adres strony www: ")

while line != "":
    webaddresses.append(line)
    line = input("Podaj adres strony www: ")

print(webaddresses)

dirname = os.getcwd()
filename = input("Podaj nazwe pliku: ")
filepath = os.path.join(dirname,filename)

file = open(filepath,"w+")

for adress in webaddresses:
    file.write(adress+"\n")

file.close()