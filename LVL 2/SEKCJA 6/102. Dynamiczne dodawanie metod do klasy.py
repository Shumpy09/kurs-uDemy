import csv
import types
#from os import write

def exportToFile_Static(path, header, data):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(data)

    print('>>> This is function exportToFile - static method')

# funkcja podpięta na poziomie klasy
def exportToFile_Class(cls, path):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # wysłanie linijki wartości. Wbudowane sa we wnętrze funkcji i nie przekazujemy ich jako argument
        writer.writerow(['brand', 'model', 'IsOnSale'])
        # z klasy, ze zmiennej zdefiniowanej na poziomie klasy (listOfCars),  zostana pobrane wszystkie instancje, które w tej chwili istnieją
        # i dla każdej z tych instancji do pliku csv zostanie wysłany osobny wiersz, info o marce, modelu i przecenie
        for c in cls.listOfCars:
            writer.writerow([c.brand, c.model, c.IsOnSale])

    print('>>> This is function exportToFile - class method')


# funkcja zdefiniowana na poziomie instancji 
def exportToFile_Instance(self, path):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # wysłanie linijki wartości. Wbudowane sa we wnętrze funkcji i nie przekazujemy ich jako argument
        writer.writerow(['brand', 'model', 'IsOnSale'])
        # z danej instancji obiektu self wybieramy właściwości brand, model, IsOnSale i wysyłamy do pliku csv
        writer.writerow([self.brand, self.model, self.IsOnSale])
        
    print('>>> This is function exportToFile - instance method')


brandOnSale = 'Opel'


class Car:

    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.__isOnsale = isOnSale
        Car.numberOfCars += 1
        Car.listOfCars.append(self)

    def IsDamaged(self):
        return not(self.isAirBagOK and self.isMechanicOK and self.isPaintingOK)

    def __GetIsOnSale(self):
        return self.__isOnsale 
    
    def __SetIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnsale = newIsOnSaleStatus
            print('Checking status IsOnSale to {} for {}'.format(newIsOnSaleStatus, self.brand))
        else:
            print('Cannot change status InOnSale. Sale valid only for {}'.format(brandOnSale))

    IsOnSale = property(__GetIsOnSale, __SetIsOnSale, None, 'if set to true, the car is available in sale/promo')
    

car_01 = Car('Seat', 'Ibiza', True, True, True, False)
car_02 = Car('Opel', 'Corsa', True, False, True, True)

print('Static-----------'*10)
Car.ExportToFile_Static = exportToFile_Static
#exportToFile_Static(r'C:\Users\Samsung\Desktop\Python\uDemy\LVL 2\SEKCJA 6\export_static.csv',['Brand', 'Model', 'IsOnSale'],[car_01.brand, car_01.model, car_01.IsOnSale])
Car.ExportToFile_Static(r'C:\Users\Samsung\Desktop\Python\uDemy\LVL 2\SEKCJA 6\export_static.csv',['Brand', 'Model', 'IsOnSale'],[car_01.brand, car_01.model, car_01.IsOnSale])

print('Class-----------'*10)
#Car.ExportToFile_Class = exportToFile_Class
# Funkcja MethodType oczekuje 2 argumentow: pierwszy to nazwa zewnętrznej funkcji, która ma być przybindowana do klasy, a drugi to nazwa klasy
Car.ExportToFile_Class = types.MethodType(exportToFile_Class, Car)
Car.ExportToFile_Class(path = r'C:\Users\Samsung\Desktop\Python\uDemy\LVL 2\SEKCJA 6\export_class.csv')

print('Instance-----------'*10)
#car_01.ExportToFile_Instance = exportToFile_Instance
car_01.ExportToFile_Instance = types.MethodType(exportToFile_Instance, car_01)
car_01.ExportToFile_Instance(path=r'C:\Users\Samsung\Desktop\Python\uDemy\LVL 2\SEKCJA 6\export_instance.csv')
