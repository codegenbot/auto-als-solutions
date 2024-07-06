def double_the_sum_of_squares(numbers):
    if len(numbers) < 2:
        raise ValueError("List should contain at least two elements.")
    numbers = sorted([num for num in numbers if isinstance(num, int) and num > 0])
    return (numbers[0] - numbers[-1]) * 2