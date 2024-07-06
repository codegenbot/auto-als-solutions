from typing import List


def concatenate(strings: List[str]) -> str:
    result = ''.join([s for s in strings if s.strip()])
    return result


strings = input("Enter strings separated by space : ").split()
print(concatenate(strings))