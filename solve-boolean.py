def solve_boolean(expression):
    if expression == 'T':
        return True
    elif expression == 'F':
        return False
    while '|' in expression:
        a, b = expression.split('|')
        expression = solve_boolean(a) and solve_boolean(b)
    while '&' in expression:
        a, b = expression.split('&')
        expression = solve_boolean(a) and solve_boolean(b)
    if expression == 'T':
        return True
    elif expression == 'F':
        return False