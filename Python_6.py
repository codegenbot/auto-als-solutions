```
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    for group in paren_string.split():
        level = 0
        nested_level = 0
        for char in group:
            if char == '(':
                level += 1
                nested_level = max(nested_level, level)
            elif char == ')':
                level -= 1
        result.append(nested_level)
    return result