```
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    for paren_group in paren_string.split():
        stack = []
        max_depth = 0
        for char in paren_group:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if stack:
                    stack.pop()
                    if len(stack) > max_depth:
                        max_depth = len(stack)
        result.append(max_depth)
    return result