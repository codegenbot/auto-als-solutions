def evaluate_boolean_expression(expression):
    expression = (
        expression.replace('t', 'True')
        .replace('f', 'False')
    )
    expression = expression.replace('&', ' and ').replace('|', ' or ')
    while ' and ' in expression:
        parts = expression.rsplit(' and ', 1)
        expression = '(' + parts[0] + ' and ' + parts[1] + ')'
    return eval(expression)

expression = input().strip().lower()
print(evaluate_boolean_expression(expression))