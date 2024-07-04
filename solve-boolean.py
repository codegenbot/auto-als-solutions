def evaluate_boolean_expression(expression):
    expression = expression.replace('t', 'T').replace('f', 'F')
    tokens = []
    i = 0
    while i < len(expression):
        if expression[i] in 'TF':
            tokens.append(expression[i] == 'T')
        elif expression[i] == '&':
            left = tokens.pop()
            right = expression[i + 1] == 'T'
            tokens.append(left and right)
            i += 1
        else:
            tokens.append(expression[i])
        i += 1
 
    result = tokens[0]
    for i in range(1, len(tokens), 2):
        if tokens[i] == '|':
            result = result or tokens[i + 1]
    return result

expression = input().strip().lower().replace(' ', '')
print(evaluate_boolean_expression(expression))