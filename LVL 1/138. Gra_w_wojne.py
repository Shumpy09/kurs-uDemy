import random

colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]

allCards = []

for c in colors:
    for f in figures:
        aCard = f.copy()
        aCard['Color'] = c
        allCards.append(aCard)

random.shuffle(allCards)
print(allCards)

player1 = []
player2 = []

max = len(allCards)
for i in range(max):           
    if i % 2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])

print("Karty player1: ", player1)
print("Karty player2: ", player2)

while len(player1) > 0 and len(player2) > 0:
    
    # wyciągnięcie karty z każdej ręki gracza
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    
    if card1["Power"] > card2["Power"]:
        
        player1.append(card1)
        player1.append(card2)
        print("Ilosc kart Player1: ", len(player1), "\nIlosc kart Player2: ", len(player2))

    elif card1["Power"] < card2["Power"]:
        
        player2.append(card2)
        player2.append(card1)
        print("Ilosc kart Player1: ",len(player1), "\nIlosc kart Player2: ", len(player2))
    else:
        print(card1, card2, "REMIS! Karty wracają do właścicieli!")
        player1.append(card1)
        player2.append(card2)
        print("Ilosc kart Player1: ",len(player1), "\nIlosc kart Player2: ", len(player2))

if len(player1) > 0:
    print("Wygral PLAYER1!!!")
else:
    print("Wygral PLAYER2!!!")




