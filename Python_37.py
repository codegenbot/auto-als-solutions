```
def sort_even(l: list):
    even_l = [x for x in l[1::2]]
    sorted_even_l = sorted(even_l)
    result = []
    index = 0
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(sorted_even_l[index])
            index += 1
        else:
            result.append(l[i])
    return result