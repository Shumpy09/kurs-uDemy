class Car:


    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.__isOnsale = isOnSale
        

    def IsDamaged(self):
        return not (self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

    def GetInfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag      - ok -       {}".format(self.isAirBagOK))
        print("Painting     - ok -       {}".format(self.isPaintingOK))
        print("Mechanic     - ok -       {}".format(self.isMechanicOK))
        print("Is on sale   - ok -       {}".format(self.__isOnsale))
        print("--------------------------")

# metody instancji, jako pierwszy argument przyjmuje self, czli tą instancje na której należy wykonać operację
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

# metoda klasy, pracuje na poziomie klasy i jako pierwszy argument przyjmuje klase, 
# nie moze operować na żadnej zmiennej zdefiniowanej na poziomie instancji, 
# ale ma dostęp do innych metod zdefiniowanych na poziomie klasy jak i innych atrybutow zdefiniowanych na poziomie klasy
# uzywamy dekoratora @classmethod
    
    # metoda klasy
    @classmethod
    def ReadFromText(cls,aText):
        aNewCar = cls(*aText.split(':'))
        return aNewCar

# metoda statyczna nie ma żadnego związku z klasą, poza tym, że się w niej znajduje.
# nie przyjmuje ani argumentu self, ani argumentu cls, wykonuje tylko czynnosci powiązane z klasą, ale nie ma tu wspolnych zmiennych czy metod
# uzywamy dekoratora @staticmethod 
    #metoda statyczna
    @staticmethod
    def Convert_KM_KW(KM):
        return KM * 0.735

    @staticmethod
    def Convert_KW_KM(KW):
        return KW * 1.36

lineOfText = "Renault:Megane:True:True:False:False"
car03 = Car.ReadFromText(lineOfText)
car03.GetInfo()

print("converting 120KM to KW: ", Car.Convert_KM_KW(120))
print("converting 90 KW to KM", Car.Convert_KW_KM(90))

