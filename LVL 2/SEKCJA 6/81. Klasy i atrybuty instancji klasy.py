# klasa próbuje połączyć w sobie zarówno dane jak i funkcje które na tych danych będą wykonywane
# kiedy powstaje opis konkretnego samochodu to mówimy że w oparciu o klase powstaje instacnaj tej klasy. Na instancje klasy często mówimy obiekt.
# instancja klasy pozwala na odwoływanie się do wszystkich własciwości które posiada klasa
# nazewnictwo: cechy opisywane przez klase - wlasciwosci, atrybuty; natomiast funkcje: metody

class Car:

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK

#instancje, obiekty
car_01 = Car('Seat','Ibiza', True, True, True)
car_02 = Car('Opel','Corsa', True, False, True)

print(car_01.brand, car_01.model, car_01.isAirBagOK, car_01.isPaintingOK, car_01.isMechanicOK)
print(car_02.brand, car_02.model, car_02.isAirBagOK, car_02.isPaintingOK, car_02.isMechanicOK)