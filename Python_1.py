def separate_paren_groups(paren_string: str) -> list:
    stack = []
    groups = []
    current_group = ""

    for char in paren_string:
        if char == " ":
            continue
        elif char == "(":
            if not stack or stack[-1] == ")":
                current_group += char
            else:
                stack.append(char)
                current_group += char
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            current_group += char
            while stack and stack[-1] != "(":
                stack.pop()
            if not stack or stack[-1] == "(":
                groups.append("(" + current_group + ")")
                current_group = ""

        elif char.isalpha() or (char.isspace() and stack):
            pass

    if stack:
        groups.append("(" + current_group + ")")

    return [g for g in groups if g]