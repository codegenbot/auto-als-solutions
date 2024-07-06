from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    result = [max(set(nums[: i + 1])) for i in range(len(nums))]
    return result