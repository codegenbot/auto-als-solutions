def solveBoolean(expression):
    def evaluate(expression):
        while "|" in expression:
            left, right = expression.split("|", 1)
            if "&" in left and "&" in right:
                return "T" if (evaluate(left[: left.index("&")]) == "True") and (evaluate(right[: right.index("&")]) == "True") else "F"
            elif "&" in left:
                return evaluate(left) == "True"
            elif "&" in right:
                return evaluate(right) == "True"
            else:
                return "T" if (evaluate(left[: left.index("|")]) == "True") or (evaluate(right[: right.index("|")]) == "True") else "F"
        while "&" in expression:
            left, right = expression.split("&", 1)
            return "T" if (evaluate(left) == "True") and (evaluate(right) == "True") else "F"
        return "T" if expression == "t" else "F"

    return evaluate(expression)