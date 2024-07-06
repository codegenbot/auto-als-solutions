```
def valid_date(date):
    if len(date) < 10:
        return False
    date_parts = date.split('-')
    if len(date_parts) != 3:
        return False
    month, day, year = map(int, date_parts)
    if not (1 <= month <= 12):
        return False
    if (month in [1, 3, 5, 7, 8, 10, 12] and 1 > day or day > 31) or \
       (month in [4, 6, 9, 11] and 1 > day or day > 30) or \
       (month == 2 and 1 > day or day > 29):
        return False
    return True