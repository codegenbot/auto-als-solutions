```
from typing import List


def concatenate(strings: List[str]) -> str:
    result = ''.join(strings)
    return result


strings = input("Enter strings separated by space : ").split()
print(concatenate(strings))