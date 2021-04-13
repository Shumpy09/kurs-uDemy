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
    stock = []

    
    if card1["Power"] == card2["Power"]:
        while card1["Power"] == card2["Power"]:
            print("WOJNA!!! Karta Player1: ", card1, "\tKarta Player2: ", card2)
            stock.append(card1)
            stock.append(card2)

            if len(player1) < 2:
                player2.extend(stock)
                player2.extend(player1)
                player1 = []
                break
        
            elif len(player2) < 2:
                player1.extend(stock)
                player1.extend(player2)
                player2 = []
                break
            
            else:
                card1 = player1.pop(0)
                card2 = player2.pop(0)
                stock.append(card1)
                stock.append(card2)
                card1 = player1.pop(0)
                card2 = player2.pop(0)
        
        else:
            if card1["Power"] > card2["Power"]:
                stock.append(card1)
                stock.append(card2)
                player1.extend(stock)

            else:
                stock.append(card1)
                stock.append(card2)
                player2.extend(stock)
    

    elif card1["Power"] > card2["Power"]:
        player1.append(card2)
        player1.append(card1)
        print("PLAY-1 \t %d \t %d \t" % (card1["Power"], card2["Power"]) + len(player1)*'*')
    else:
        player2.append(card1)
        player2.append(card2)
        print("PLAY-2 \t %d \t %d \t" % (card1["Power"], card2["Power"]) + len(player2)*'*')

if len(player1) > 0:
    print("PLAYER-1 WON!!!!")
else:
    print("PLAYER-2 WON!!!!")
