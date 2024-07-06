def intersperse(numbers: list[int], delimiter: int) -> list[int]:
    if not numbers:
        return []
    result = [numbers[0]]
    for i in range(1, len(numbers)):
        result.extend([delimiter, numbers[i]])
    if delimiter != numbers[-1]:
        result.append(delimiter)
    return result