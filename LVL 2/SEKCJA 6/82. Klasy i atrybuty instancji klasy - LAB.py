class Cake:
    
    def __init__(self, name, kind, taste, addictions, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.addictions = addictions
        #self.addictions = addictives.copy()
        self.filling = filling


#cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
#cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '')
#cake03 = Cake('Super Sweet Merigue', 'merigue', 'very sweet', [], '')

cake_01 = Cake('ciasto1','urodzinowe','czekoladowy','truskawka','masa kakaowa')
cake_02 = Cake('ciasto2','urodzinowe2','czekoladowy2','truskawka2','masa kakaowa2')
cake_03 = Cake('ciasto3','urodzinowe3','czekoladowy3','truskawka3','masa kakaowa3')

#bakery_offer = []
#bakery_offer.append(cake_01)
#bakery_offer.append(cake_02)
#bakery_offer.append(cake_03)

bakery_offer = [cake_01, cake_02, cake_03]

print('Today in our offer:')
for c in bakery_offer:
    print('{} - ({}) main taste: {} with additives of [{}], filled with {}'.format(c.name, c.kind, c.taste, c.addictions, c.filling))