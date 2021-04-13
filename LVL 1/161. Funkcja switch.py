def WeekDayInPoland(dayNumber):
    names = {
        0: 'Poniedziałek',
        1: 'Wtorek',
        2: 'Środa',
        3: 'Czwartek',
        4: 'Piątek',
        5: 'Sobota',
        6: 'Niedziela'
    }

    return names.get(dayNumber,"error")

print(WeekDayInPoland(4))