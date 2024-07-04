def solve_boolean(expression):
    expression = expression.replace("t", "True").replace("f", "False").replace("&", " and ").replace("|", " or ")
    return eval(expression)

# Read input from user
expression = input().strip()
print(solve_boolean(expression))