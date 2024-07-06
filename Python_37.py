```python
def sort_even(l: list):
    even = sorted((x, y) for x, y in zip(l[1::2], l[::2]))
    return [x if i % 2 != 0 else y for i, (x, y) in enumerate(even)]