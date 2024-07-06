def rolling_max(numbers: List[int]) -> List[int]:
    max_until_now = [max(range(1, i + 1)) for i in range(len(numbers))]
    return [max(max_until_now[: i + 1]) for i in range(len(numbers))]