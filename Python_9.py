from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    result = [max(nums) for nums in zip(*[iter(numbers)] * i + [numbers])]
    return result