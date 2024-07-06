def sort_even(l: list):
    even = sorted([x for x in l if x % 2 == 0])
    odd = [x for x in l if x % 2 != 0]
    
    return [x if i < len(odd) else even[i - len(odd)] for i, x in enumerate(l)]