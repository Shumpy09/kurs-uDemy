import random
'''
myNumbers = []

while len(myNumbers) < 7:

    newNumber = random.randint(1,49)

    if newNumber in myNumbers:
        print("Ta liczba zostala juz wylosowana!: ", newNumber)
        continue

    myNumbers.append(newNumber)

print(myNumbers)
'''
# listy kolorów i figur
colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
figures = ['Ace', 'King', 'Queen', 'Jack', '10', '9']


allCards = []

# zagnieżdżona pętla łączenia kolorów i figur
for x in colors:
    for y in figures:
        card = x + y              # łącznie koloru i figury
        allCards.append(card)     # dodanie karty do listy allCards
        # allCards.append("%s - %s" % (c, f))

print(allCards)

# tasowanie kart
random.shuffle(allCards)
print(allCards)

# rozdanie
player1 = []
player2 = []


# sposob 1
'''
max = len(allCards)

for i in range(0, max-1):           # for i in range(max):
    if i % 2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])

print("Karty player1: ", player1)
print("Karty player2: ", player2)
'''
# sposob 2

player1 = allCards[:12]
player2 = allCards[12:]

print("Karty player1: ", player1)
print("Karty player2: ", player2)


