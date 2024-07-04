def evaluate_boolean_expression(expression):
    expression = (
        expression.replace("t", "True")
        .replace("f", "False")
        .replace("&", " and ")
    )
    while ' and ' in expression:
        expression = eval('(' + ') and ('.join(expression.split(' and ')) + ')')
        
    expression = expression.replace("|", " or ")
    return eval(expression)

expression = input().strip().lower()
print(evaluate_boolean_expression(expression))