from typing import List

def longest(strings: List[str]) -> str:
    if not strings:
        raise ValueError("No strings provided")
    return max(strings, key=len)