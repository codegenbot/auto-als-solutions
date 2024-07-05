```
from typing import List


def concatenate(strings: List[str]) -> str:
    if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
        return "Invalid input format"
    return ''.join(strings)