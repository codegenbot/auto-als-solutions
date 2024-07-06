def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    current_max = 0
    for char in paren_string:
        if char == '(':
            current_max += 1
        elif char == ')':
            current_max -= 1
        result.append(current_max)
    return result