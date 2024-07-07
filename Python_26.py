def remove_duplicates() -> list[int]:
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    return sorted(list(set(numbers)))