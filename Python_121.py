def solution(lst):
    """Complete this code to sum all odd numbers starting from second element of the list."""
    return sum(i for i in lst[1:] if i % 2 != 0)