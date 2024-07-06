from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    level = 0
    for char in paren_string:
        if char == '(':
            if level > 0:
                result.append(-1)
                level -= 1
            else:
                result.append(1)
                level = 1
        elif char == ')':
            result.append(-1)
            level -= 1
    return result