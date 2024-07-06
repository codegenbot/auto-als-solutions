def rolling_max(numbers: List[int]) -> List[int]:
    result = []
    max_seen_so_far = numbers[0]
    for num in numbers:
        result.append(max_seen_so_far)
        max_seen_so_far = max(max_seen_so_far, num)
    return result