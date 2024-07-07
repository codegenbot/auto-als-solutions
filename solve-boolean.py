```
def solve_boolean(expression):
    if expression == 'T':
        return True
    elif expression == 'F':
        return False
    else:
        operator = '&' if '&' in expression else '|'
        left_expression = expression.split(operator)[0]
        right_expression = expression.split(operator)[1]
        return solve_boolean(left_expression) if operator == '&' else (not solve_boolean(left_expression))