```
def sort_even(l):
    even_elements = sorted([x for x in l if x % 2 == 0])
    odd_indices = [i for i in range(len(l)) if i % 2 != 0]
    return [even_elements.pop(0) if i % 2 != 0 else (y for y in even_elements).next() if even_elements else None for i, _ in enumerate(l)]