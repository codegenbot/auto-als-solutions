def sort_numbers(numbers: str) -> str:
    nums = [int(i.split()[0][:-3]) for i in numbers.split()]
    return " ".join(sorted(map(str, set(nums))))