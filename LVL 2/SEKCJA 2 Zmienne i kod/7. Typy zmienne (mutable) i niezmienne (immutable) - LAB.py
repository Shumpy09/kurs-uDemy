days = ['mon','tue','wed','thu','fri','sat','sun']

workdays = days.copy()
workdays.remove('sat')
workdays.remove('sun')

# workdays = workdays[:-2]

print("days: ",days)
print("workdays: ",workdays)