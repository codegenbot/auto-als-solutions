```
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    if len(numbers) == 0:
        return 0
    total = sum(abs(num) for num in numbers)
    count = len([num for num in numbers if isinstance(num, (int, float))])
    if count == 0:
        return 0
    return total / count