def solve(input_string):
    if input_string == 'T':
        return True
    elif input_string == 'F':
        return False
    elif '&' in input_string:
        op1, op2 = input_string.split('&')
        return not (solve(op1) and solve(op2))
    elif '|' in input_string:
        op1, op2 = input_string.split('|')
        return solve(op1) or solve(op2)
    else:
        raise ValueError("Invalid Boolean expression")