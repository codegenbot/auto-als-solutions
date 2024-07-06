```
def valid_date(date):
    month, day, year = date.split('-')
    if len(month) < 1 or len(day) < 1 or len(year) < 4:
        return False
    try:
        int_month = int(month)
        int_day = int(day)
        int_year = int(year)
    except ValueError:
        return False
    if int_month < 1 or int_month > 12:
        return False
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    if int_month == 2 and (int_year % 4 != 0 or (int_year % 100 == 0 and int_year % 400 != 0)):
        days_in_month[1] = 28
    elif int_month in [4,6,9,11]:
        days_in_month[3-1] = 30
    elif int_month == 12:
        if (int_year % 4 == 0 and int_year % 100 != 0) or (int_year % 400 == 0):
            days_in_month[1] = 29
    if int_day < 1 or int_day > days_in_month[int_month-1]:
        return False
    return True