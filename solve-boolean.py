def solve_boolean(expression):
    if expression == 'T':
        return True
    elif expression == 'F':
        return False
    while '|' in expression:
        a, b = expression.split('|')
        expression = str(solve_boolean(a)) and str(solve_boolean(b))
    while '&' in expression:
        a, b = expression.split('&')
        expression = str(solve_boolean(a)) and str(solve_boolean(b))
    if expression == 'T':
        return True
    elif expression == 'F':
        return False