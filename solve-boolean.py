import re

def evaluate_boolean_expression(expression):
    expression = expression.replace("t", "True").replace("f", "False")
    expression = re.sub(r'(\b(True|False)\b)&(\b(True|False)\b)', r'(\1 and \3)', expression)
    expression = expression.replace("|", " or ")
    return eval(expression)

expression = input().strip().lower()
print(evaluate_boolean_expression(expression))