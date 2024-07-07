def solveBoolean(expression):
    if expression == "t":
        return True
    elif expression == "f":
        return False
    elif "&" in expression:
        left, right = expression.split("&")
        return bool(int(left)) & bool(int(right))
    elif "|" in expression:
        left, right = expression.split("|")
        return bool(int(left)) | bool(int(right))