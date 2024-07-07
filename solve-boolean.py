def solveBoolean(expression):
    def evaluate(expression):
        while "|" in expression:
            left, right = expression.split("|", 1)
            return "T" if (evaluate(left) == "True") or (evaluate(right) == "True") else "F"
        while "&" in expression:
            left, right = expression.split("&", 1)
            return "T" if (evaluate(left) == "True") and (evaluate(right) == "True") else "F"
        return "T" if expression == "t" else "F"

    return evaluate(expression)