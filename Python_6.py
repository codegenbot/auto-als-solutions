from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    level = 0
    temp_result = []
    for char in paren_string:
        if char == '(':
            level += 1
            temp_result.append(level)
        elif char == ')':
            level -= 1
            temp_result.append(level)
            result.append(temp_result)
            temp_result = []
    return result