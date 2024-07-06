from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    if not numbers:
        return 0
    median = (
        sorted([num for num in numbers if isinstance(num, (int, float))])[
            len(numbers) // 2
        ]
        if len(numbers) % 2 != 0
        else sum(sorted([num for num in numbers if isinstance(num, (int, float))]))
        / len([num for num in numbers if isinstance(num, (int, float))])
    )
    return sum(abs(num - median) for num in numbers) / len(numbers)