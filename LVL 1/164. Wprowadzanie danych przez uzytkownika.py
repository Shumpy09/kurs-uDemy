while True:
    
    filesizeStr = input("Enter the max file size (MB): ")
    if filesizeStr.isdecimal():
        fileSizeInt = int(filesizeStr)
        break

print("The max size is %d" % (fileSizeInt))

print("Size in KB is %d" % (fileSizeInt *1024))
