def sort_numbers(numbers: str) -> str:
    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
                'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    nums = [num_dict[i] for i in numbers.split()]
    sorted_nums = sorted(nums)
    return ' '.join([f'{"zero" if num == 0 else "one" if num == 1 else "two" if num == 2 else "three" if num == 3 else "four" if num == 4 else "five" if num == 5 else "six" if num == 6 else "seven" if num == 7 else "eight" if num == 8 else "nine"' for num in sorted_nums])