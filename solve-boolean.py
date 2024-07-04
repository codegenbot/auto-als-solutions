def solve_boolean(expression):
    expression = expression.replace("t", "True").replace("f", "False")
    return eval(expression)


# Read input from user
expression = input().strip()
print(solve_boolean(expression))