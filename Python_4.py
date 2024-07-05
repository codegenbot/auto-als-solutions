from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    if not numbers:
        return "Error: Empty list"

    for num in numbers:
        if not isinstance(num, (int, float)):
            return "Error: List contains non-numeric values"

    mean = sum(numbers) / len(numbers)
    total_deviation = sum(abs(num - mean) for num in numbers)

    return total_deviation / len(numbers)