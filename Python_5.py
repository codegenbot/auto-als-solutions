def intersperse(numbers: list[int], delimiter: int) -> list[int]:
    result = []
    if len(numbers) > 1:
        result.append(numbers[0])
        for i in range(1, len(numbers)):
            result.extend([result[-1], delimiter, numbers[i]])
    else:
        result = [numbers[0]]
    return result