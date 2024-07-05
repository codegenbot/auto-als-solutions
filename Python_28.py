from typing import List

def concatenate(strings: List[str]) -> str:
    return ''.join(strings)

input_strings = input("Enter some strings separated by space or press enter when done: ").split()
print(concatenate(input_strings))