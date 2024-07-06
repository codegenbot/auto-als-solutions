```
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    stack = []
    group = ""
    for char in paren_string:
        if char == " ":
            continue
        if char == "(":
            stack.append(char)
            group += char
        elif char == ")":
            if stack:
                stack.pop()
                group += char
            else:
                result.append(group + ")")
                group = ""
    if stack:
        while stack:
            group += ")"`
            stack.pop()
        result.append(group)
    else:
        result.append(group)
    return [result[0].split() if result else []]