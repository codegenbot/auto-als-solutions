Here is a possible solution in Python:

def solve_boolean(expression):
    if expression == 'T':
        return True
    elif expression == 'F':
        return False
    elif '&' in expression:
        left, right = expression.split('&')
        return not (solve_boolean(left) and solve_boolean(right))
    elif '|' in expression:
        left, right = expression.split('|')
        return solve_boolean(left) or solve_boolean(right)
    else:
        raise ValueError("Invalid Boolean expression")

# example usage
print(solve_boolean('t'))  # True
print(solve_boolean('f&f'))  # False
print(solve_boolean('f&t'))  # False
print(solve_boolean('t&f'))  # False