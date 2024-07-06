from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    if len(numbers) == 0:
        return 0
    total = sum(num for num in numbers if isinstance(num, (int, float)))
    count = len([num for num in numbers if isinstance(num, (int, float))])
    mean = total / count if count > 0 else 0

    return (
        sum(abs(num - mean) for num in numbers if isinstance(num, (int, float))) / count
        if count > 0
        else 0
    )