from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    stack = []
    current_group = ""

    for char in paren_string:
        if char == " ":
            continue
        if char in ["(", "[", "{"]:
            stack.append(char)
            current_group += char
        elif char in [")", "]", "}"]:
            if stack and stack.pop() == "(":
                current_group += char
            else:
                groups.append(current_group)
                current_group = ""

    if stack:
        groups.append(current_group)
    else:
        groups.append(current_group)

    return [group[1:-1] for group in groups]