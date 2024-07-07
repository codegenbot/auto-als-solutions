````
def remove_duplicates() -> List[int]:
    """Remove duplicates from a list of integers entered by the user."""
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    return sorted(list(set(numbers)))