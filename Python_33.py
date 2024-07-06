```python
def sort_third(lst: list):
    return [x if i % 3 != 0 else sorted([y for y in lst[:i//3*3] + lst[i//3*3+1:] if (i-1) // 3 * 3 + j % 3 == i])[j] 
            for i in range(len(lst)) 
            for j in range(3)]