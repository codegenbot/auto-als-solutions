```python
def sort_third(lst):
    return sorted([x if isinstance(x, list) else [x] if x % 3 == 0 else [x] for x in lst])