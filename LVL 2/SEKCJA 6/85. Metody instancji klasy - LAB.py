class Cake:
    
    def __init__(self, name, kind, taste, addictions, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.addictions = addictions.copy()
        self.filling = filling

    def show_info(self):
        print("Name:        {}".format(self.name).upper())
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if self.addictions:
            print("Addictions:  {}".format(self.addictions))
      # if len(self.addictions) > 0:
      #     print("Additives: ")
      #     for a in self.addictions:
      #         print("\t{}".format(a))
        if self.filling:
            print("Filling:     {}".format(self.filling))
      # if len(self.filling) > 0:
      #     print("Filling:     {}".format(self.filling))
        print("--------------------------")

    def set_filling(self, filling):
        self.filling = filling
        
    def add_additives(self, addictions):
        self.addictions = addictions.copy()
      # self.addictions.extend(addictions)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '')
cake03 = Cake('Super Sweet Merigue', 'merigue', 'very sweet', [], '')

cake02.set_filling("vanilla cream")
cake03.add_additives(["cocoa powder", "coconuts"])

cake01.show_info()
cake02.show_info()
cake03.show_info()


#cake_01 = Cake('ciasto1','urodzinowe','czekoladowy','truskawka','masa kakaowa')
#cake_02 = Cake('ciasto2','urodzinowe2','czekoladowy2','truskawka2','masa kakaowa2')
#cake_03 = Cake('ciasto3','urodzinowe3','czekoladowy3','truskawka3','masa kakaowa3')

#bakery_offer = []
#bakery_offer.append(cake01)
#bakery_offer.append(cake02)
#bakery_offer.append(cake03)

bakery_offer = [cake01, cake02, cake03]
'''
print('Today in our offer:')
for c in bakery_offer:
    print('{} - ({}) main taste: {} with additives of [{}], filled with {}'.format(c.name, c.kind, c.taste, c.addictions, c.filling))
'''
