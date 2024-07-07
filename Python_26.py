from typing import List

def remove_duplicates() -> List[int]:
    input_list = list(map(int, input("Enter numbers separated by space: ").split()))
    return sorted(list(set(input_list)))