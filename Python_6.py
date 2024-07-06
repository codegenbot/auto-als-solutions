from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    level = 0
    temp_list = []
    for char in paren_string:
        if char == '(':
            temp_list.append(level)
            level += 1
        elif char == ')':
            temp_list.append(level)
            level -= 1
        temp_list.append(level)
    return [temp_list]