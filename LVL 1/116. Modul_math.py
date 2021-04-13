import math

degree = 360
print(math.radians(degree))
print(degree * math.pi/180)

degree = 45
print(math.radians(degree))
print(degree * math.pi/180)

small_pizza_r = 0.22
big_pizza_r = 0.27
family_pizza_r = 0.38

small_pizza_price = 11.50
big_pizza_price = 15.60
family_pizza_price = 22.00

small_pizza_area = math.pi * math.pow(small_pizza_r, 2)
big_pizza_area = math.pi * math.pow(big_pizza_r, 2)
family_pizza_area = math.pi * math.pow(family_pizza_r, 2)

print('Small pizza:','\nCena: ',small_pizza_price,'\nRozmiar[m]: ', small_pizza_r,'\nPole: ', small_pizza_area)
print('Big pizza:','\nCena: ',big_pizza_price,'\nRozmiar[m]: ', big_pizza_r,'\nPole: ', big_pizza_area)
print('Family pizza:','\nCena: ',family_pizza_price,'\nRozmiar[m]: ', family_pizza_r,'\nPole: ', family_pizza_area)

print("Metr kwadratowy small pizza: ", small_pizza_area/small_pizza_price)
print("Metr kwadratowy big pizza: ", big_pizza_area/big_pizza_price)
print("Metr kwadratowy family pizza: ", family_pizza_area/family_pizza_price)

math_ls = dir(math)
print(math_ls)
