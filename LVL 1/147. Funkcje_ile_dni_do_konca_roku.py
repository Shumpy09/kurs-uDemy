from datetime import date

def DaysToEndOfYear(year = date.today().year,
                    month = date.today().month, 
                    day = date.today().day):
    
    date_today = date.today()
    current_year = date_today.year
    date_end_year = date(current_year, 12, 31)
    delta = date_end_year - date_today

    print(delta.days)

    return delta.days


iloscdni = DaysToEndOfYear()
print("Ilosc dni do konca: ",iloscdni)
#DaysToEndOfYear(2020,12,20)
#DaysToEndOfYear(day = 23, month = 8, year = 1993)
#DaysToEndOfYear()
#DaysToEndOfYear(year = 2021, month = 2)
#DaysToEndOfYear(day = 9)