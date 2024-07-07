from typing import List

def remove_duplicates() -> List[int]:
    numbers_str = input("Enter numbers separated by space: ")
    numbers = list(map(int, numbers_str.split()))
    return sorted(list(set(numbers)))