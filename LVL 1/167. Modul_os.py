import os
import time

print("Current directory is:", os.getcwd())
# wyświetl bieżący katalog

currentDir = os.getcwd()
filename = "results.txt"
fullpath = os.path.join(currentDir,filename)
print("The constructed file path is: ", fullpath)
# zapisanie pliku w aktualnym katalogu

relativePath = 'output.txt'
print("The absolute path is: ", os.path.abspath(relativePath))
# absolutna wartość ścieżki, razem z literą dysku

filepath = r'c:\temp\results.txt'
print("The file name part is: ", os.path.basename(filepath)) # zwroci nazwe pliku
print("The directory part is: ", os.path.dirname(filepath)) # zwróci ściezke do katalogu

print("Is file existing? ", os.path.exists(filepath))

if os.path.exists(filepath):
    print("Last modify date is: ", os.path.getmtime(filepath))
    print("Last modify date is: ", time.localtime(os.path.getmtime(filepath)))

    print("File size is: ", os.path.getsize(filepath))

    print("Is it a file?: ", os.path.isfile(filepath))
    print("Is it a dir?: ", os.path.isdir(filepath))

    print("Path splitted: ", os.path.split(filepath))
    print("Only file name part: ", os.path.split(filepath)[1])

    print("Path splitted into drive: ", os.path.splitdrive(filepath))
    print("Only drive: ", os.path.splitdrive(filepath)[0])
