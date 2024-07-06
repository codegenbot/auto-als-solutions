```
def sort_even(l: list):
    evens = sorted([x for x in l if x % 2 == 0])
    new_list = []
    even_index = 0
    for i, x in enumerate(l):
        if x % 2 != 0:
            new_list.append(x)
        else:
            new_list.append(evens[even_index])
            even_index += 1
    return new_list