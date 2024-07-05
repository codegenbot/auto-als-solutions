def evaluate_boolean_expression(expression):
    tokens = expression.replace('t', 'True').replace('f', 'False').split('|')
    evaluated_tokens = [eval(token.replace('&', ' and ')) for token in tokens]
    return any(evaluated_tokens)

expression = input().strip().lower()
print(evaluate_boolean_expression(expression))