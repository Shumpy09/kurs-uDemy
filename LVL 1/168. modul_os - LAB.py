import os
import time

dir = input("Wprowadź ścieżke do katalogu: ")

if not os.path.isdir(dir):
    print("%s nie jest scieżką" % dir)
else:
    file = input("Wprowadź nazwę pliku w katalogu %s: " % dir)

    path = os.path.join(dir, file)
    print(path)

    if not os.path.isfile(path):
        print("Plik %s nie istnieje" % path)
    else:
        print("Właściwości pliku %s: " % path)
    # print("Data ostatniej modyfikacji: ", os.path.getmtime(path))
    # print("Data ostatniej modyfikacji: ", time.localtime(os.path.getmtime(path)))
        print("Rozmiar pliku: ", os.path.getsize(path))
        print("Bieżący katalog: ", os.getcwd())
        print("Relatywna ścieżka: ", os.path.relpath(path))
