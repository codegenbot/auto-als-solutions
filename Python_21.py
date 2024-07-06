from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    if not numbers:
        return []  # Return an empty list for an empty input
    return [(x - min(numbers)) / (max(numbers) - min(numbers)) for x in numbers]