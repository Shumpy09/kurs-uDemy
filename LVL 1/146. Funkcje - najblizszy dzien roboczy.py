def GiveWorkingDay():
    from datetime import date
    from datetime import timedelta

    day = date.today()
    #day  = date(2021,2,8)

    if day.weekday() = 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() = 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day

    print("working day for ", day, " is ", workingday)

    return

GiveWorkingDay()