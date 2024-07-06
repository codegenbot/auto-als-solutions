```Python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
"""Parse a string of nested parentheses into an integer list where '1' means opening parenthesis and '-1' means closing parenthesis.
"""
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