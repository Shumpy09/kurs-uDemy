file_path = r"c:\Users\Samsung\Desktop\Python\uDemy\Folder1\data_input\orders.csv.txt"

with open(file_path,'r') as file:
    for line in file:
        
        line = line.replace("\n", " ")
        order = line.split(",")
        
        print(line)
        print(order)

        if len(order) == 3:
            print("Order from drugstore %s, item %s, amount %s" % (order[0], order[1], order[2]))
        
        else:
            print("Line %s malformed!!!" % line)

print("Koniec przetwarzania danych")    