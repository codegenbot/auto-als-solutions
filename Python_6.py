```
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """Parse a string containing nested parentheses and return a list of integers representing the levels."""
    result = []
    level = 0
    for char in paren_string:
        if char == '(' and level == 0:
            result.append(1)
            level = 1
        elif char == ')' and level > 0:
            result.append(-1)
            level -= 1
        elif level < 0:
            break
    return result