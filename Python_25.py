```
def get_max_min_average():
    numbers = input("Enter some numbers (space separated): ").split()
    numbers = [int(num) for num in numbers]

    if not numbers:
        return "No numbers entered."

    max_num = max(numbers)
    min_num = min(numbers)
    average = sum(numbers) / len(numbers)

    return f"Max: {max_num}, Min: {min_num}, Average: {average}"

print(get_max_min_average())