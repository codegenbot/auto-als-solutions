```
def parse_nested_parens(paren_string: str) -> List[int]:
    result = []
    level = 0
    max_level = 0
    temp_result = []
    for char in paren_string:
        if char == '(':
            level += 1
            temp_result.append(level)
            max_level = max(max_level, level)
        elif char == ')':
            level -= 1
            temp_result.pop()
    result.extend(temp_result)
    return result