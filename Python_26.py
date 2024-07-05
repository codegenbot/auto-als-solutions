from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = {}
    return [seen.get(x, x) for x in numbers]