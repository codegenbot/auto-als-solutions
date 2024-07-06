```
def sum_squares(lst):
    total = 0
    for num in lst:
        if (lst.index(num) + 1) % 3 == 0:
            total += num ** 2
        elif (lst.index(num) + 1) % 4 == 0 and not (lst.index(num) + 1) % 3 == 0:
            total += num ** 3
    return total