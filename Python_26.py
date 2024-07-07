```
def remove_duplicates() -> List[int]:
    """Remove duplicates from a list of integers"""
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    return sorted(list(set(numbers)))