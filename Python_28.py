from typing import List


def concatenate(strings: List[str]) -> str:
    result = "".join(strings)
    return result


strings = input("Enter strings separated by space : ")
try:
    strings = strings.split()
except ValueError as e:
    print(f"Error: {str(e)}")
print(concatenate(strings))