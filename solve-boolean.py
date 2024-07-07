def solve_boolean(expression):
    def evaluate_operator(a, b, operator):
        if operator == "&":
            return a and b
        elif operator == "|":
            return a or b
        else:
            raise ValueError("Invalid operator")

    result = True  # assume True initially
    operators = ["&", "|"]
    for i in range(len(expression) - 1):
        if expression[i] in operators:
            a = expression[i - 1] == "T"
            b = expression[i + 1] == "T"
            result = evaluate_operator(a, b, expression[i])
    return result