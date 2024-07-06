from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    if len(numbers) == 0:
        return 0
    total = 0.0
    count = 0
    mean = 0
    for num in numbers:
        if isinstance(num, (int, float)):
            total += num
            count += 1
            mean = total / count if count > 0 else 0
        else:
            raise ValueError("Invalid input: non-numeric value found")
    return sum(abs(num - mean) for num in numbers) / count if count > 0 else 0