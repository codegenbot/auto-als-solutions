def evaluate_boolean_expression(expression):
    expression = (
        expression.replace('T', ' True ')
        .replace('F', ' False ')
        .replace('|', ') or (')
        .replace('&', ' and ')
    )
    expression = '(' + expression + ')'
    return eval(expression)

expression = input().strip().upper()
print(evaluate_boolean_expression(expression))