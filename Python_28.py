```
from typing import List


def concatenate(strings: List[str]) -> str:
    result = ''.join(strings)
    return result


strings = input("Enter strings separated by space : ").split()
try:
    print(concatenate(strings))
except ValueError as e:
    print("Invalid input. Please enter strings separated by spaces.")