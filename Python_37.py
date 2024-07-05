Here is the modified code:

def sort_even(l: list):
    return [x if i % 2 != 0 else sorted([y for y in l if i % 2 == 0 and y < x])[0] if [y for y in l if i % 2 == 0 and y < x] else None for i, x in enumerate(l)]