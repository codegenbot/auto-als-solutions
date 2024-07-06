def find_sum_of_odd_elements_in_alternating_sublist(lst):
    total = 0
    for i in range(1, len(lst), 2):
        total += lst[i]
    return total