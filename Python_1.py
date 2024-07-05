from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    groups = []
    current_group = ''

    for char in paren_string:
        if char == ' ':
            continue
        if char == '(':
            stack.append(char)
            current_group += char
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
                if not stack:  # Check if stack is empty
                    groups.append(current_group)
                    current_group = ''
            else:
                current_group += char

    return groups