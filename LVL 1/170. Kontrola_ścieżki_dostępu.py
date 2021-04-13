import os


fileIsOk = False

while not fileIsOk:
    filename = input("Enter path to results file: ")

    if os.path.isfile(filename):
        fileIsOk = True


print("The results file is: %s" % (filename))

# 2
"""
import os

while True:
    filename = input("Enter the path to results: ")

    if os.path.isfile(filename):
        break
    else:
        print("File name is not correct, try again!")

print("The results file is: %s" % (filename))
"""