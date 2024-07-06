def mean_absolute_deviation(numbers: List[float]) -> float:
    if len(numbers) == 0:
        return 0
    total = 0.0
    count = 0
    mean = 0
    for num in numbers:
        if isinstance(num, (int, float)):
            total += num
            count += 1
            mean = total / count if count > 0 else 0
        else:
            raise ValueError("Invalid input: non-numeric value found")
    return sum(abs(num - mean) for num in numbers) / count if count > 0 else 0


def main():
    num_list = []
    while True:
        try:
            num = float(input("Enter a number (or 'done' to finish): "))
            if num == float("inf") or num == -float("inf"):
                raise ValueError("Invalid input: Please do not enter infinity.")
            num_list.append(num)
        except ValueError as e:
            print(f"Error: {str(e)}")
            break
    return mean_absolute_deviation(num_list)


print(main())