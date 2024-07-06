def sort_numbers(numbers: str) -> str:
    num_dict = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    sorted_num = [""] * len(numbers.split())
    for word in numbers.split():
        if word in num_dict:
            sorted_num[num_dict[word]] = word
    return " ".join(sorted_num).lstrip()