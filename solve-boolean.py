```
def solve_boolean(expression):
    def evaluate_operator(a, b, operator):
        if operator == "&":
            return a and b
        elif operator == "|":
            return a or b
        else:
            raise ValueError("Invalid operator")

    def evaluate_expression(expression):
        stack = []
        result = True
        operators = ["&", "|"]
        i = 0
        while i < len(expression):
            if expression[i] in "TF":
                if not stack:
                    result = expression[i] == "T"
                else:
                    a = stack.pop() == "T"
                    operator = stack.pop()
                    if operator == "&":
                        result = result and a
                    elif operator == "|":
                        result = result or a
            elif expression[i] in operators:
                stack.append(expression[i])
                stack.append(result)
                result = True
            i += 1
        return result

    return evaluate_expression(expression)