#from typing import Text


class Cake:
    
    known_kinds = ['cake','muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'prezel', 'other']
    bakery_offer = []
    

    def __init__(self, name, kind, taste, addictions, filling, gluten_free, text):
        
        self.name = name 
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.addictions = addictions.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print('Kind is not cake or empty string')

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
        print("Gluten free: {}".format(self.__gluten_free))
      #  print("Text:        {}".format(Text))
        if len(self.__text) > 0:
            print("Text:        {}".format(self.__text))
        print("--------------------------")

    def set_filling(self, filling):
        self.filling = filling
        
    def add_additives(self, addictions):
        self.addictions.extend(addictions)
    
    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('Kind is not cake or empty string')

    Text = property(__get_text, __set_text, None, 'if set is true, the text on cake is available')

cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, 'Happy BDay!')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', False, '<3')
cake03 = Cake('Super Sweet Merigue', 'merigue', 'very sweet', [], '', True, '')
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False, 'Happy Happy!')

print('Today in our offer:')
for c in Cake.bakery_offer:
    c.show_info()

cake01.Text = 'Happy Birthday!'
cake02.Text = '18'

for c in Cake.bakery_offer:
    c.show_info()

