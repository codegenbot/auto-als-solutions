```
def solution(lst):
    return sum(i for i in lst[::2] if i % 2 != 0) + (lst[0] if lst[0] % 2 != 0 else 0)