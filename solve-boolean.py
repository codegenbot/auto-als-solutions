def evaluate_boolean_expression(expression):
    expression = (
        expression.replace('t', 'True')
        .replace('f', 'False')
    )
    expression = expression.replace('&', ' and ').replace('|', ' or ')
    while ' and ' in expression:
        pos = expression.rfind(' and ')
        left = eval(expression[:pos].replace(' or ', ' or (') + ')')
        right = eval(expression[pos+5:].replace(' or ', ' or (') + ')')
        expression = ' or '.join(str(left and right) + ')')
    return eval(expression)

expression = input().strip().lower()
print(evaluate_boolean_expression(expression))