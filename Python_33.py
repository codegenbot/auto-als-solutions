def 'sort_third'(lst):
    sorted_list = sorted(lst, key=lambda x: x[2])
    return sorted_list