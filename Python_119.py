```
def match_parens(lst):
    open_count = 0
    for string in lst:
        open_count += string.count('(') - string.count(')')
        if open_count < 0:
            return "No"
    return "Yes" if open_count == 0 else "No"