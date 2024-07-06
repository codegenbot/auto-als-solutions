```
from typing import List


def mean_absolute_deviation() -> float:
    numbers = []
    while True:
        num_str = input("Enter a number (or 'done' to finish): ")
        if num_str.lower() == 'done':
            break
        try:
            num = float(num_str)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid number or type 'done' to finish.")
    return calculate_mad(numbers)


def calculate_mad(numbers: List[float]) -> float:
    if not isinstance(numbers, list):
        return "Error: Invalid input"
    if len(numbers) == 0:
        return 0
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    total = sum(numeric_numbers)
    count = len(numeric_numbers)
    mean = total / count if count else 0
    return sum(abs(num - mean) for num in numeric_numbers) / count if count else 0