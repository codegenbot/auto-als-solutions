```Python
def solve_boolean(expression):
    def evaluate_expression(expression):
        if not expression: return None  # base case: empty string

        if expression[0] == "(":
            i = expression.index(")")
            return evaluate_expression(expression[1:i])  # recursive call to evaluate sub-expression

        a = expression[0] == "T"
        operator = ""
        for i in range(1, len(expression)):
            if expression[i].in(["&", "|"]):
                if operator: 
                    if not operator: return a
                    if operator == "&": return a and True
                    if operator == "|": return a or True
                else:
                    operator = expression[i]
                break

        b = evaluate_expression(expression[i+1:])  # recursive call to evaluate sub-expression
        if operator == "&": return a and b
        if operator == "|": return a or b
        raise ValueError("Invalid operator")

    return evaluate_expression(expression)