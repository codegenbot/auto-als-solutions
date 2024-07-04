def evaluate_boolean_expression(expression):
    expression = (
        expression.replace("t", "(True)")
        .replace("f", "(False)")
        .replace("&", ") and (")
        .replace("|", ") or (")
    )
    expression = '(' + expression + ')'
    return eval(expression)

expression = input().strip().lower()
print(evaluate_boolean_expression(expression))