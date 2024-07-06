```
def match_parens(lst):
    for string in lst:
        open_count = 0
        close_count = 0
        for char in string:
            if char == '(':
                open_count += 1
            elif char == ')':
                if open_count == 0:
                    return "No"
                open_count -= 1
        if open_count != 0:
            return "No"
    return "Yes"