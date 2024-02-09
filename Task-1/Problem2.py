def days_in_month(month, year):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    elif year % 4:  # check leap year
        return 28
    else:
        return 29


def tmr_date(day, month, year):
    if day < days_in_month(month, year):
        return day + 1, month, year
    elif month < 12:
        return 1, month + 1, year
    else:
        return 1, 1, year + 1


x = int(input("Day: "))
y = int(input("Month: "))
z = int(input("Year: "))
tmr_day, tmr_month, tmr_year = tmr_date(x, y, z)
print(f"Day: {tmr_day} Month: {tmr_month} Year: {tmr_year}")
