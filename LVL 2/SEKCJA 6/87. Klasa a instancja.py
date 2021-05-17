class Car:

    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        Car.numberOfCars += 1
        Car.listOfCars.append(self)

    def IsDamaged(self):
        return not (self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

    def GetInfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag  - ok -       {}".format(self.isAirBagOK))
        print("Painting - ok -       {}".format(self.isPaintingOK))
        print("Mechanic - ok -       {}".format(self.isMechanicOK))
        print("--------------------------")

print("Class level variables BEFORE creating instances: ", Car.numberOfCars, Car.listOfCars)

#instancje, obiekty
car_01 = Car('Seat','Ibiza', True, True, True)
car_02 = Car('Opel','Corsa', True, False, True)

print("Class level variables AFTER creating instances: ", Car.numberOfCars, Car.listOfCars)

print("Id of class is: ", id(Car))                                             # sprawdzanie ID classy
print("Id of instances are: ", id(car_01), id(car_02))                         # sprawdzanie ID instancji klasy Car

print("Check if object belongs to calss: ", isinstance(car_01, Car))           # czy dana instancja należy do danej klasy
print("Check if object belongs to class using type: ", type(car_01) is Car)    # czy obiekt należy do klasy, uzywajac type
print("Check class of an object using __class__:", car_01.__class__)           # czy instancja nalezy do klasy, uzywajac __class__

print("List of instance attributes with values: ", vars(car_01))               # zobaczenie funkcji 'od srodka'; info dostepne jako slownik
print("List of instance attributes with values: ", vars(Car))

print("List of instances attributes with values: ", dir(car_01))
print("List of instances attributes with values: ", dir(Car))

# liczba samochodow zmieni sie
Car.numberOfCars = 123 

print("value taken from instances: ", car_01.numberOfCars, "Value taken from class: ",Car.numberOfCars)