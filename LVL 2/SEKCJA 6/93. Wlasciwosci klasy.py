
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
        return not (self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

    def GetInfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag      - ok -       {}".format(self.isAirBagOK))
        print("Painting     - ok -       {}".format(self.isPaintingOK))
        print("Mechanic     - ok -       {}".format(self.isMechanicOK))
        print("Is on sale   - ok -       {}".format(self.__isOnsale))
        print("--------------------------")

# odczytanie wartosci atrybutu
    def __GetIsOnSale(self):
        return self.__isOnsale

# zmiana wartosci atrybutu
    def __SetIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnsale = newIsOnSaleStatus
            print('Checking status IsOnSale to {} for {}'.format(newIsOnSaleStatus, self.brand))
        else:
            print('Cannot change status InOnSale. Sale valid only for {}'.format(brandOnSale))


    IsOnSale = property(__GetIsOnSale, __SetIsOnSale, None, 'if set to true, the car is available in sale/promo')

#instancje, obiekty
car_01 = Car('Seat','Ibiza', True, True, True, False)
car_02 = Car('Opel','Corsa', True, False, True, True)


'''
print('Status of cars: ', car_01.__GetIsOnSale(), car_02.__GetIsOnSale())

car_01.SetIsOnSale(True)
car_02.SetIsOnSale(False)
print('Status of cars: ', car_01.__GetIsOnSale(), car_02.__GetIsOnSale())
'''

car_01.IsOnSale = True
car_02.IsOnSale = True
print('Status of cars: ', car_01.IsOnSale, car_02.IsOnSale)
