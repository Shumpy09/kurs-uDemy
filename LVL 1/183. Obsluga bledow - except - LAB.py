import sys
 
file_path = r'c:\Users\Samsung\Desktop\Python\uDemy\Folder1\data_input\orders.csv.txt'
 
 
with open(file_path,"r") as file:
 
    for line in file:
 
        line = line.replace('\n','')
        order = line.split(',')
 
        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
            print('Order from drugstore "%s", item "%s", amount %d' %
                      (pharmacy_name, item, amount))

        except ValueError as e:
            print("Błąd konwersji danych w linii: %s " % line)
            print(line)
        except IndexError as e:
            print("Niedostateczna ilość pól z danymi w linii: %s " % line)
            print(line)
        except:
            print("Problem with line %s" % line)
            print(sys.exc_info()[0])
 
print("Processing finished")