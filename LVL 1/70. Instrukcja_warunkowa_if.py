min_likes = 500
min_shares = 100
num_likes = 1300
num_shares = 550

if num_likes >= min_likes and num_shares >= min_shares:
    print('Wystarczajaca ilosc likeow i shareow. Ceny nizsze o 10%!')
else:
    print("Niewystarczająca ilość like'ów lub share'ów.")

isPizzaOrdered = True
isBigDrinkOrdered = True
isWeekend = True

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print('Zamówiłeś pizze lub duzy napoj w dzien roboczy - otrzymujesz kupon na burgera!')
else:
    print('Nie otrzymujesz kuponu')

diskSize = 140      # ilosc GB
diskSizeUsed = 133  # zajete miejsce
fileSize = 10      # wielkosc pliku

if (diskSize-diskSizeUsed) > fileSize:
    print('File can be downloaded')
else:
    print('File can\'t be downloaded')
