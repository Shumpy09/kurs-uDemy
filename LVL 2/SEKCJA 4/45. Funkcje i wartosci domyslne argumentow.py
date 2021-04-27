def BuyMe(prefix = 'Please buy me', what = 'a new car'):                                #deklaracja funkcji
    print(prefix,what)

BuyMe('Please buy me', 'a new car')                     #wywołanie funkcji, przekazywanie wartosci argumentu przez pozycje

BuyMe(prefix = 'Please buy me', what = 'a car')     #wywolanie funkcji, przekazywanie wartosci argumentu przez nazwe
BuyMe(what = 'a dog', prefix = 'Please buy me')
BuyMe('Please')
BuyMe(prefix='Please buy me')
BuyMe(what='a new car')

# ustawiajac wartosci domyslne, trzeba je podac albo wszystkie, albo zadne
