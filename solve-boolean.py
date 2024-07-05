def evaluate_boolean_expression(expression):
    import re
    while '&' in expression:
        expression = re.sub(r'(t|f)&(t|f)', lambda m: '({} and {})'.format(m.group(1), m.group(2)), expression)
    expression = (
        expression.replace('t', 'True')
        .replace('f', 'False')
        .replace('|', ' or ')
        .replace('&', ' and ')
    )
    return eval(expression)

expression = input().strip().lower()
print(evaluate_boolean_expression(expression))