def sort_even(l: list):
    even = [x for x in l if x % 2 == 0]
    odd = sorted([x for x in l if x % 2 != 0])

    return [
        even[i // 2] if i < len(even) else odd[i - len(even)] for i in range(len(l))
    ]