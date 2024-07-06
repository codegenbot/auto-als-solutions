def sum_squares(lst):
    total = 0
    for num in lst:
        if isinstance(num, int) and abs(num) <= 10:
            total += num**2
    return total