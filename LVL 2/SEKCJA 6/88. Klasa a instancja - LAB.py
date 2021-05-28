class Cake:
    
    known_kinds = ['cake','muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'prezel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, addictions, filling):
        
        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.addictions = addictions.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        

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
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa')

print('Today in our offer:')
for c in Cake.bakery_offer:
    c.show_info()


#cake02.set_filling("vanilla cream")
#cake03.add_additives(["cocoa powder", "coconuts"])


print("Sprawdzanie czy obiekt cake01 jest instancja klasy Cake korzystając z funkcji isinstance", isinstance(cake01, Cake))
print("Sprawdzanie czy obiekt cake01 jest instancja klasy Cake korzystajac z funkcji type", type(cake01) is Cake)
print("Info o instancji cake01", vars(cake01))
print("Info o instancji Cake", vars(Cake))
print("Info o instancji cake01", dir(cake01))
print("Info o instancji Cake", dir(Cake))