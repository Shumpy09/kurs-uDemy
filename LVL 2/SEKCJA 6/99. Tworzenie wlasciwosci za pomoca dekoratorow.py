brandOnSale = 'Opel'

class Car:


    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.__isOnsale = isOnSale
        

    @property
    def IsOnSale(self):
        return self.__isOnsale 

    @IsOnSale.setter
    def IsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnsale = newIsOnSaleStatus
            print('Checking status IsOnSale to {} for {}'.format(newIsOnSaleStatus, self.brand))
        else:
            print('Cannot change status InOnSale. Sale valid only for {}'.format(brandOnSale))

    @IsOnSale.deleter
    def IsOnSale(self):
        self.__isOnsale = None

car_01 = Car('Seat', 'Ibiza', True, True, True, False)
print(car_01.IsOnSale)
car_01.IsOnSale = True
