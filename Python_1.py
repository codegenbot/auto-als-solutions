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
                if not stack:  
                    groups.append(current_group)
                    current_group = ''
            else:
                if stack:  # Unmatched opening parenthesis, add to group
                    current_group += ')'
                else:      # Unmatched closing parenthesis, treat as new group
                    groups.append('('+current_group+')')
                    current_group = ''

    if stack and current_group:  # Last unmatched opening parenthesis
        groups.append('('+current_group+')')

    return [g for g in groups if g]