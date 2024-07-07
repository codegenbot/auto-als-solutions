```
from typing import List


def remove_duplicates() -> List[int]:
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    return sorted(list(set(numbers)))