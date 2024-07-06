```
from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    result = [max(numbers[: i + 1]) for i in range(len(numbers))]
    print("Enter a list of numbers separated by spaces:")
    input_numbers = list(map(int, input().split()))
    return result