```
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    groups = []
    current_group = ""

    for char in paren_string:
        if char == " ":
            continue
        elif char == "(":
            stack.append(char)
            current_group += char
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
                if not stack:
                    groups.append(current_group + ")")
                    current_group = ""
            else:
                if current_group:  
                    groups.append("(" + current_group + ")")
                    current_group = ""

        elif char.isalpha() or (char.isspace() and stack): 
            pass

    while stack and stack[-1] == "(":
        stack.pop()

    if stack:
        while stack:
            stack.pop()
        groups.append("(" + current_group + ")")

    return [g for g in groups if g]