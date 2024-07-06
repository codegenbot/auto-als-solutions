Problem: 
This problem can be solved using Python programming. The problem description is not available for this problem.

def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    stack = []
    max_level = 0
    for char in paren_string:
        if char == '(':
            stack.append(char)
            max_level += 1
        elif char == ')':
            stack.pop()
            max_level -= 1
        if not stack and max_level > 0:
            result.append(max_level)
            max_level = 0
    return result