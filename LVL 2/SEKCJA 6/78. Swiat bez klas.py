# klasa to słownik z kluczami i watościami
# 

car_01 = {
'carBrand' : 'Seat',
'carModel' : 'Ibiza',
'carIsAirBagOK' : True,
'carIsPaintingOK' : True,
'carIsMechanicOK' : True
}

car_02 = {
'carBrand' : 'Opel',
'carModel' : 'Corsa',
'carIsAirBagOK' : True,
'carIsPaintingOK' : False,
'carIsMechanicOK' : True
}
# skoro teraz wszystkie argumenty są zapisane jako jedna zmienna(słownik), to możnemy do funkcji przekazać słownik
def IsCarDamaged(aCar):
# funkcja sprawdzająca będzie zaglądać do tego słownika i przeglądać wartości określonych funkcji
    return not (aCar['carIsAirBagOK'] and aCar['carIsPaintingOK'] and aCar['carIsMechanicOK'])

# funkcje mozna wywoływac odwołując się tylko do kluczy słownika

print(IsCarDamaged(car_01))
print(IsCarDamaged(car_02))

# obiekty mozemy przechowywac w liście 
cars = [car_01, car_02]

for c in cars:
# odwołując się do wartości kluczy, stosujemy notacje: wskaznujemy na slownik c['nazwa klucza']
    print("{} {} damaged = {}".format(c['carBrand'], c['carModel'], IsCarDamaged(c)))
