```
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    if not numbers:
        return 0
    mean = sum(numbers) / len(numbers)
    total_deviation = sum(abs(num - mean) for num in numbers)
    return total_deviation / len(numbers)