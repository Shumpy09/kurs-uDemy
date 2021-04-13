min_likes = 1000
min_shares = 500

num_likes = 1200
num_shares = 600


if num_likes >= min_likes and num_shares >= min_shares:
    print('Wszystko sie zgadza')
elif num_likes <= min_likes:
    print('Niewystarczająca ilość like\'ów')
else:
    print('Niewystarczająca ilośc share\'ów!')


isPizzaOrdered = False
isBigDrinkOrdered = False
isWeekend = False

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print('Wszystko się zgadza')
elif isWeekend:
    print('Jest weekend')
else:
    print('Nie zamowiles pizzy lub napoju')
