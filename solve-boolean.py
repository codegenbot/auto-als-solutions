def solve_boolean(expression):
    if expression == "T":
        return True
    elif expression == "F":
        return False
    elif "&" in expression:
        a, b = expression.split("&")
        return solve_boolean(a) and solve_boolean(b)
    elif "|" in expression:
        parts = []
        current_part = ""
        for char in expression:
            if char in ["|", "&"]:
                parts.append(current_part)
                current_part = ""
                parts.append(char)
            else:
                current_part += char
        return (
            (solve_boolean(parts[0]) or solve_boolean(parts[2]))
            if parts[1] == "|"
            else (solve_boolean(parts[0]) and solve_boolean(parts[2]))
        )