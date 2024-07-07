from typing import List


def remove_duplicates():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    return [key for key in dict.fromkeys(numbers).keys()]