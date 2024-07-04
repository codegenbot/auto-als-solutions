def solve_boolean(expression):
    expression = expression.replace('t', 'True').replace('f', 'False').replace('&', ' and ').replace('|', ' or ')
    return eval(expression)

expression = input().strip()
print(solve_boolean(expression))