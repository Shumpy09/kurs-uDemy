def BuyMe(prefix = 'Please buy me', what = 'a new car', *args, **kwargs):
    print(prefix,what)
    print(args)
    print(kwargs)

BuyMe('Please buy me', 'a new car', 'a cat', 'a dog', 'a dragon', shop='market', color='yellow') 

products = ['milk', 'bread', 'flakes']
parameters = {'price':'low', 'time':'now'}

BuyMe('Buy me', 'newspaper', *products, **parameters)




# *args - moze byc dowolne inne slowo, najwazniejsza jest *
# *args to tuplet, czyli lista z wartosciami
# *args przyjmuje dowolna ilosc argumentow

# **kwargs - argumenty poprzedzone nazwa, argument poprzedzony slowem kluczowym
# **kwargs to slownik
