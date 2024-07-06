```
from typing import List


def concatenate() -> str:
    num_strings = int(input("Enter number of strings: "))
    strings = []
    
    for _ in range(num_strings):
        s = input("Enter string: ")
        strings.append(s)
        
    result = ""
    for s in strings:
        result += s
    return result

print(concatenate())