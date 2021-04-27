'''def Log_it(*args):
    filename = r'C:\Users\Samsung\Desktop\Python\uDemy\LVL 2\SEKCJA 4\lab49a.txt'
    
    line = str(args)
    file = open(filename, 'a')
    file.write(line)
    file.write("\n")
    
    file.close()

Log_it("Starting processing forecasting")
Log_it("Error", "Not enough data", "invoices", "2020")'''



def log_it(*args):
    path = r'C:\Users\Samsung\Desktop\Python\uDemy\LVL 2\SEKCJA 4\lab49a.txt'
    with open(path, "a") as f:
        for line in args:
            f.write(line)
            f.write(' ')

        f.write("\n")

log_it("Starting processing forecasting")
log_it("Error", "Not enough data", "invoices", "2020")