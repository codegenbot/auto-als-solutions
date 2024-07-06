from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    if not paren_string:
        return []
    stack = []
    groups = []
    current_group = ""

    for char in paren_string:
        if char == " ":
            continue
        if char == "(":
            stack.append(char)
            current_group += char
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
                if not stack:  # Check if stack is empty
                    groups.append(current_group)
                    current_group = ""
            else:
                groups.append(
                    "(" + current_group + ")"
                )  # Unmatched closing parenthesis, treat as new group
                current_group = ""

    if stack:  # Handle unmatched opening parentheses at the end of the string
        while stack and stack[-1] == "(":
            stack.pop()
        groups.append("(" + current_group + ")")

    return [g for g in groups if g]