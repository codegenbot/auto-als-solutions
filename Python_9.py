from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    result = [max(set(x)) for x in (list(y) for y in ([*numbers])]
    return result