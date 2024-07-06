def sum_squares(lst):
    return sum(i ** ((i + 2) // 3) if i % 4 == 0 else i for i in lst)