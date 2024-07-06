```
def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    level = 0
    for char in paren_string:
        if char == '(' and level > 0:
            result.append(1)
        elif char == ')' and level < 1:
            break
        elif char == '(':
            level += 1
            result.append(-1)
        elif char == ')':
            level -= 1
            result.append(1)
    return result