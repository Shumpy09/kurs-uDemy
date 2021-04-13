price = 123
bonus = 23
bonus_granted = True

'''
if bonus_granted:
    price -= bonus

print(price)
'''
price = price - bonus if bonus_granted else price
print(price)

# zadanie 2

rating = 5
'''
if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')
'''
print('very good' if rating == 5 else 'good' if rating == 4 else 'weak')


# zadanie 3
from datetime import date

today_weeday = date.today().strftime("%A")
print(today_weeday)
'''
if today_weeday == 'Monday':
    print('Pomagam mamie')
elif today_weeday == 'Tuesday':
    print('pranie')
elif today_weeday == 'Wednesday':
    print('pranie')
elif today_weeday == 'Thursday':
    print('dyżur')    
elif today_weeday == 'Friday':
    print('2 zebrania')
elif today_weeday == 'Saturday':
    print('lekcje')
else:
    print('Niedziela będzie dla nas')
'''
print('Pomagam mamie' if today_weeday == 'Monday' else 'pranie' if today_weeday == 'Tuesday' else 'pranie' if today_weeday == 'Wednesday' else 'dyżur' if today_weeday == 'Thursday' else '2 zebrania' if today_weeday == 'Friday' else 'lekcje' if today_weeday == 'Saturday' else 'Niedziela bedzie dla nas')

