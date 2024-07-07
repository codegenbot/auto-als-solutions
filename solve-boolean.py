```
def solve_boolean(expression):
    if expression == 'T':
        return True
    elif expression == 'F':
        return False
    elif '&' in expression:
        a, b = expression.split('&')
        return solve_boolean(a) and solve_boolean(b)
    elif '|' in expression:
        while'|' in expression or '&' in expression':
            if '|' in expression:
                a, b = expression.split('|',1)
                expression = str(solve_boolean(a)) and str(solve_boolean(b))
            elif '&' in expression:
                a, b = expression.split('&',1)
                expression = str(solve_boolean(a)) and str(solve_boolean(b))
        return eval(expression)