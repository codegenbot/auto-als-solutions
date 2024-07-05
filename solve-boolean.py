def evaluate_boolean_expression(expression):
    expression = (
        expression.replace('T', 'true')
        .replace('F', 'false')
        .replace('|', ' or ')
        .replace('&', ' and ')
    )
    return eval(expression)

expression = input().strip()
print(evaluate_boolean_expression(expression))