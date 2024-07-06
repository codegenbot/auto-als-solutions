```
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    stack = []
    for char in paren_string:
        if char == '(':
            stack.append(1)
        elif char == ')':
            level = sum(stack)
            result.append(level)
            while len(stack) > 0 and stack[-1] != 1:
                stack.pop()
            stack.pop()
    return result