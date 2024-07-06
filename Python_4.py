from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("No numbers were provided")
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    total = sum(numeric_numbers)
    count = len(numeric_numbers)
    mean = total / count
    return sum(abs(num - mean) for num in numeric_numbers) / count