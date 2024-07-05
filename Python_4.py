from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    if not numbers:
        return "Error: Empty list"

    for num in numbers:
        if not isinstance(num, (int, float)):
            return "Error: Non-numeric value in the list"