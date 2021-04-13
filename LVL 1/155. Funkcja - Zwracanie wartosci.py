from datetime import date
from datetime import timedelta

def GiveWorkingDay(year = date.today().year, 
                   month = date.today().month, 
                   day = date.today().day):
    

    #day = date.today()
    day  = date(year, month, day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    return workingday

nextworkingday = GiveWorkingDay(2021,2,7)
print("Next working day after",2021,2,7,"is",nextworkingday)
nextworkingday = GiveWorkingDay()
print("Next working day after today is", nextworkingday)

print("Next working day aftertoday is", GiveWorkingDay())
