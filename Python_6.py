```
from typing import List
stack = []
result = []
def parse_nested_parens(paren_string: str) -> List[int]:
    for paren in paren_string.split():
        level = 0
        for char in paren:
            if char == '(':
                stack.append(char)
                level += 1
            elif char == ')':
                stack.pop()
                level -= 1
        result.append(level)
    return result