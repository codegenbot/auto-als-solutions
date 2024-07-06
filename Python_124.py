```
def valid_date(date):
    parts = date.split('-')
    month, day, year = map(int, parts[:2]) + [int(year)]
    if len(parts) != 3 or len(str(month)) > 2 or len(str(day)) > 2:
        return False
    if not (1 <= month <= 12):
        return False
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if not (1 <= day <= 31):
            return False
    elif month == 2:
        if not (1 <= day <= 29):
            return False
    elif month in [4, 6, 9, 11]:
        if not (1 <= day <= 30):
            return False
    return True