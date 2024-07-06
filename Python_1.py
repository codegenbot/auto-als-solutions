Here is the corrected Python code:

```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    stack = []
    group = ''
    
    for char in paren_string:
        if char == ' ':
            continue
        if char == '(':
            stack.append(char)
            group += char
        elif char == ')':
            if stack:
                stack.pop()
                group += char
                if not stack:
                    result.append(group[1:])
                    group = ''
            else:
                return []  # invalid input
    
    if group:
        result.append(group)
    
    return result