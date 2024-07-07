def solve_boolean(expression):
    if expression == "T":
        return True
    elif expression == "F":
        return False
    else:
        i = expression.find("&")
        if i != -1:
            a = expression[:i]
            b = expression[i + 1 :]
            return solve_boolean(a) and solve_boolean(b)
        else:
            i = expression.find("|")
            if i != -1:
                a = expression[:i]
                b = expression[i + 1 :]
                return solve_boolean(a) or solve_boolean(b)
            else:
                return True