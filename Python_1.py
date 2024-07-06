```
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    current_group = ''
    level = 0
    for char in paren_string:
        if char == ' ': continue
        if char == '(':
            level += 1
            current_group += '('
        elif char == ')':
            level -= 1
            current_group += ')'
            if level == 0: result.append(current_group)
            current_group = ''
    return result