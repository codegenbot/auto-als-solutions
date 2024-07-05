def sort_even(l: list):
    even = [x for x in l if x % 2 == 0]
    odd = sorted([x for x in l if x % 2 != 0])

    result = []
    i, j = 0, 0

    while i < len(even) or j < len(odd):
        if i >= len(even):
            result.append(odd[j])
            j += 1
        elif j >= len(odd):
            result.append(even[i])
            i += 1
        elif even[i] < odd[j]:
            result.append(even[i])
            i += 1
        else:
            result.append(odd[j])
            j += 1

    return tuple(result)