import re

def evaluate_boolean_expression(expression):
    expression = re.sub(r'\bT\b', 'True', expression)
    expression = re.sub(r'\bF\b', 'False', expression)
    expression = expression.replace('|', ' or ').replace('&', ' and ')
    return eval(expression)

expression = input().strip()
print(evaluate_boolean_expression(expression))