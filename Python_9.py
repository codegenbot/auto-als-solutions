```Python
def max_rolling_sum(numbers: list[int]) -> int:
    if not numbers:
        return 0

    start = end = current_sum = numbers[0]
    max_sum = numbers[0]

    for num in numbers[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
        start = min(start, current_sum - num)

    return max_sum