```
def valid_date(date):
    day, month, year = map(int, date.split('-'))
    if not date or len(date) != 10:
        return False
    if month < 1 or month > 12:
        return False
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month == 2 and day > days_in_month[1]:
        return False
    elif month in (1,3,5,7,8,10,12) and day > days_in_month[0]:
        return False
    elif month in (4,6,9,11) and day > days_in_month[3]:
        return False
    elif month == 2 and day < 1:
        return False
    elif (month in (1,3,5,7,8,10,12) and day < 1) or (month in (4,6,9,11) and day < 1) or (month == 2 and day < 1):
        return False
    else:
        return True