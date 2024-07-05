from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    total_difference = sum(abs(num - mean) for num in numbers)
    return total_difference / len(numbers)