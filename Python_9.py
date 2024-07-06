from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    result = [max(i) for i in zip(*[iter(numbers)] * (1 + len(numbers) // 2))]
    return result