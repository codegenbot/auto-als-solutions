def solveBoolean(expression):
    if expression == "t":
        return True
    elif expression == "f":
        return False

    if "&" in expression:
        left, right = expression.split("&", 1)
        return bool(solveBoolean(left)) and bool(solveBoolean(right))

    if "|" in expression:
        left, right = expression.split("|", 1)
        return bool(solveBoolean(left)) or bool(solveBoolean(right))

    return False