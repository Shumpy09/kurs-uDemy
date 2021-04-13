file = open("c:\\Users\\Samsung\\Desktop\\Python\\uDemy\\Folder1\\aaa.txt.txt","r") #otwarcie pliku

content = file.read()   # przeczytanie pliku
print(content)  #wyswietlenie zawartosci

file.close()    # zamkniece pliku


with open('c:\\Users\\Samsung\\Desktop\\Python\\uDemy\\Folder1\\aaa.txt') as file:
    content = file.read()
    print(content)


with open('c:\\Users\\Samsung\\Desktop\\Python\\uDemy\\Folder1\\aaa.txt.txt') as file:
    for line in file:
        print(line)

file = open('c:\\Users\\Samsung\\Desktop\\Python\\uDemy\\Folder1\\aaa.txt','r')
for line in file:
    print(line)
file.close()

# readlines przeczyta naraz cały plik do pamięci i następnie podzieli na kolekcje napisów
file = open('c:\\Users\\Samsung\\Desktop\\Python\\uDemy\\Folder1\\aaa.txt','r')
for line in file.readlines():
    print(line)
file.close()

file = open('c:\\Users\\Samsung\\Desktop\\Python\\uDemy\\Folder1\\aaa.txt','r')

fragment = file.read(10)
while fragment:
    print(file.tell(), fragment)
    fragment = file.read(10)

file.close()

