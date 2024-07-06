```
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    if not isinstance(numbers, list):
        return "Error: Invalid input"
    if len(numbers) == 0:
        return 0
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    total = sum(numeric_numbers)
    count = len(numeric_numbers)
    mean = total / count if count else 0
    return sum(abs(num - mean) for num in numeric_numbers) / count if count else 0