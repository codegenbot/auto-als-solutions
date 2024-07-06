from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    level = 0
    sublist = []
    for char in paren_string:
        if char == '(':
            level += 1
            sublist.append(level)
        elif char == ')':
            level -= 1
            sublist.append(level)
            if level == 0:  
                result.append(sublist)
                sublist = []
    return result