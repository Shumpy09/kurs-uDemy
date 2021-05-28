# cos jak zmienne publiczne i prywatne w c++
# nazwa ukrywanego atrybutu zaczyna się podwójnym podkreśleniem __, ale nie konczy sie
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


#instancje, obiekty
car_01 = Car('Seat','Ibiza', True, True, True, False)
car_02 = Car('Opel','Corsa', True, False, True, True)

car_02.__isOnsale = False
# ponizsza instrukcja zmodyfikuje wartosc
# car_02._Car__isOnsale = False

car_02.YearOfProduction = 2005
del car_02.YearOfProduction

setattr(car_02,'TAXI',False)
delattr(car_02,'TAXI')
print(hasattr(car_02,'TAXI'))

car_02.GetInfo()
print(vars(car_02))