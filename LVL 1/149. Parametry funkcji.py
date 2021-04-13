def GiveWorkingDay(year, month, day):
    from datetime import date
    from datetime import timedelta

    #day = date.today()
    day  = date(year, month, day)

    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    print("working day for ", day, " is ", workingday)

    return

GiveWorkingDay(2021,2,8)
GiveWorkingDay(year = 2021, month = 2, day = 8)
GiveWorkingDay(day = 8, month = 2, year = 2021)