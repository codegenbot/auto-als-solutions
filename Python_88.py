def sort_array(array):
    if not array:
        return []
    total = sum([array[0], array[-1]])
    if total % 2 != 0:
        return sorted(array)
    else:
        return sorted(array)[::-1]