from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    if len(numbers) == 0:
        return 0
    median = sorted([num for num in numbers if isinstance(num, (int, float))])[len(numbers)//2] if len(numbers) > 1 else numbers[0]
    total = sum(abs(num - median) for num in numbers)
    count = len([num for num in numbers if isinstance(num, (int, float))])
    return total / count