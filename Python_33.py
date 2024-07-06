def sort_third_list(lst):
    if len(lst) < 3:
        return lst
    third_elements = [item[2] for item in lst]
    return sorted(third_elements)