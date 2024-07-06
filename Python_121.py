def get_even_index_elements(lst):
    result = [element for index, element in enumerate(lst) if index % 2 == 1]
    return result