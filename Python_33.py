def sort_third_list(lst):
    sorted_lst = sorted((i for i in enumerate(lst) if i[1][2]), key=lambda x: x[1])
    return [sublist for sublist in map(lambda x: x[1], sorted_lst)]