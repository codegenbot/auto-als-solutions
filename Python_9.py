def rolling_max(numbers: List[int]) -> List[int]:
    result = []
    max_until_now = numbers[0]
    for num in numbers:
        result.append(max_until_now)
        max_until_now = max(max_until_now, num)
    return result