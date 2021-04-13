import random

'''
for i in range(0,10):
    print(random.randint(1,100))
'''
'''
number1 = random.randint(1,100)

counter = 1
number2 = random.randint(1,100)

print(number1, counter, number2)

while number2 != number1:
    print(counter,". ", number2)
    counter += 1
    number2 = random.randint(1,100)
    
print("Number1: %d, Number2: %d, Counter: %d" % (number1, number2, counter))
'''

countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]

random.shuffle(countries)
print(countries)

groupNumber = 0

for i in range(len(countries)):
    if i % 4 == 0:
        groupNumber += 1
        print("----Grupa %d----" % (groupNumber))
    
    print(countries[i])


