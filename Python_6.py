```
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    level = 0
    inside_parentheses = False
    
    for char in paren_string:
        if char == '(' and not inside_parentheses:
            result.append(1)
            level += 1
            inside_parentheses = True
        elif char == ')' and inside_parentheses:
            result.append(-1)
            level -= 1
            inside_parentheses = level > 0
        elif inside_parentheses:
            if char == '(':
                level += 1
            else:
                level -= 1
                if level < 0:
                    break
    
    return result