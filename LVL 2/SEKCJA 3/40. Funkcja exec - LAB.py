import os
files_to_process = [
    r"C:\Users\Samsung\Desktop\Python\uDemy\LVL 2\SEKCJA 3\math_sin_square.py",
    r"C:\Users\Samsung\Desktop\Python\uDemy\LVL 2\SEKCJA 3\math_square_root.py"
    ]

for file_path in files_to_process:
    with open(file_path, 'r') as f:
        print("File {} ...".format(os.path.basename(file_path)))
        source = f.read()
        exec(source)

'''
import os

files_to_process = [
    r"C:\Users\Samsung\Desktop\Python\uDemy\LVL 2\SEKCJA 3\math_sin_square.py",
    r"C:\Users\Samsung\Desktop\Python\uDemy\LVL 2\SEKCJA 3\math_square_root.py"
    ]

print("First file name: ", os.path.basename(files_to_process[0]))
print("Second file name: ", os.path.basename(files_to_process[1]))

file = open("C:\\Users\\Samsung\\Desktop\\Python\\uDemy\\LVL 2\\SEKCJA 3\\math_sin_square.py")
source = file.read()
result = exec(source)

file = open("C:\\Users\\Samsung\\Desktop\\Python\\uDemy\\LVL 2\\SEKCJA 3\\math_square_root.py")
source = file.read()
result = exec(source)
'''
