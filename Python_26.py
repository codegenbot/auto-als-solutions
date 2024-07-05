from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    if len(set(numbers)) != len(numbers):
        return "Error: The input list contains duplicates."
    else:
        return list(set(numbers))