def evaluate_boolean_expression(expression):
    expr = expression.replace(" ", "")
    result = []
    i = 0
    while i < len(expr):
        if expr[i] in 'TF':
            result.append('True' if expr[i] == 'T' else 'False')
        elif expr[i] == '&':
            result.append(' and ')
        elif expr[i] == '|':
            result.append(' or ')
        i += 1
    return eval(''.join(result))

expression = input().strip().upper()
print(evaluate_boolean_expression(expression))