filename = 'c:\\Users\\Samsung\\Desktop\\Python\\uDemy\\Folder1\\data_output\\zapis.txt'

line = 'Europe'
cities = ['London', 'Berlin', 'Paris', 'Warsaw', 'Madrid', 'Rome']

file = open(filename,'w')       #'a' append doda wartosc, a nie zastapi calosci, w+ mozna zapisac i odczytac

file.write(line)             # dopisanie wartosci
file.write("\n")
#file.writelines(cities)     # dopisanie listy wartosci

for city in cities:
    file.write(city+"\n")

file.close()