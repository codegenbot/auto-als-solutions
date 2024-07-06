def valid_date(date):
    parts = date.split('-')
    if len(parts) != 3:
        return False

    month, day, year = map(int, parts)
    if not (1 <= month <= 12 and 1 <= day <= 31):
        return False

    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month == 2:
        if day < 1 or day > (29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28):
            return False
    elif day < 1 or day > days_in_month[month - 1]:
        return False

    return True