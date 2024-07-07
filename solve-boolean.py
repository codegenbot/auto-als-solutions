def solve_boolean(expression):
    if expression == "T":
        return True
    elif expression == "F":
        return False
    operators = "|&"
    for op in operators:
        if op in expression:
            left, right = expression.split(op)
            return (
                (solve_boolean(left) or solve_boolean(right))
                if op == "|"
                else (solve_boolean(left) and solve_boolean(right))
            )