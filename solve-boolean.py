def evaluate_boolean_expression(expression):
    expression = expression.replace("&", ") and (").replace("|", ") or (")
    expression = expression.replace("t", "True").replace("f", "False")
    expression = "(" + expression + ")"
    return eval(expression)

expression = input().strip().lower()
print(evaluate_boolean_expression(expression))