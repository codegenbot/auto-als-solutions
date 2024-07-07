from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = {i: False for i in numbers}
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result[num] = True
    return list(seen)