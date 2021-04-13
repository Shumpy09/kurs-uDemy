import os

def NumberOfWords(path):
    with open(path,'r') as f:
        content = f.read()
        words = len(content.split())
        #print(words)
    return words


path = r'c:\Users\Samsung\Desktop\Python\plik1.txt'

if os.path.exists(path): # .isfile
    print("Ilosc slow w pliku: ", NumberOfWords(path))
    print('There are {} words in the file {}'.format(NumberOfWords(path), path))

os.path.isfile(path) and print('There are {} words in the file {}'.format(NumberOfWords(path),path))
