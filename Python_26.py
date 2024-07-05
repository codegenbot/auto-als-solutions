from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = {}
    result = [seen.setdefault(x, x) for x in numbers]
    print(result)
    return result