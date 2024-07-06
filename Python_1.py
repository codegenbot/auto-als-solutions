def separate_paren_groups(paren_string: str) -> list:
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
                groups.append(current_group + ")")
                current_group = ""
            else:
                if stack:
                    pass
                else:
                    groups.append("(" + current_group + ")")
                    current_group = ""

        elif char.isalpha():
            while stack and stack[-1].isalpha():
                current_group += stack.pop()
            current_group += char
        elif char.isspace() and stack:
            pass

    while stack:
        if stack[-1] == "(":
            break
        current_group += stack.pop()
    groups.append("(" + current_group + ")")

    return [g for g in groups if g]