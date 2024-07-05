from typing import list

def intersperse(numbers: list, delimeter: int) -> list:
    if len(numbers) == 0:
        return []
    result = [numbers[0]]
    for num in numbers[1:]:
        result.extend([num, delimeter])
    return result