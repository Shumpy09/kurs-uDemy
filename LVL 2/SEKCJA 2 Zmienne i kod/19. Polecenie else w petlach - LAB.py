import os
import urllib.request

data_dir = r'c:\Users\Samsung\Desktop\Python'
pages = [
    {'name':'mobilo',       'url':'http://www.mobilo24.eu/'},
    {'name':'nonexistent',  'url':'http://abc.cde.fgh.ijk.pl/'},
    {'name':'kursy',        'url':'http://kursyonline24.eu/'}]

for page in pages:
    
    try:
        file_name = "{}.html".format(page["name"])
        path = os.path.join(data_dir, file_name)

        print("Processing: {} => {} ...".format(page["url"], file_name))
        urllib.request.urlretrieve(page["url"], path)
        print("... done")
    except:
        print("Błąd w przetwarzaniu strony: {}".format(page["name"]))
        print("Zatrzymanie procesu przetwarzania")
        break

else:
    print("Program zakończony")

