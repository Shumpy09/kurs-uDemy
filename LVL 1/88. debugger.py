'''number = 1
previous_number = 0

while number < 50 :
    print(number + previous_number)
    previous_number = number
    number += 1
'''

text = ''
number = 10
condition = True

while condition :
    text += 'x'
    print(text)

    if len(text) > number :
        condition = False
