```
from typing import List


def remove_duplicates(user_input: str):
    numbers = list(map(int, user_input.split()))
    return sorted(list(set(numbers)))