from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    if len(numbers) == 0:
        return []
    
    return [(n - min(numbers)) / (max(numbers) - min(numbers)) for n in numbers]