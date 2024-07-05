import re

def evaluate_boolean_expression(expression):
    expression = re.sub(r'(\w)&(\w)', r'(\1 and \2)', expression.replace('T', 'True').replace('F', 'False'))
    expression = expression.replace('|', ' or ')
    return eval(expression)

expression = input().strip().upper()
print(evaluate_boolean_expression(expression))