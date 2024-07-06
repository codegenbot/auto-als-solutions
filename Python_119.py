```
def match_parens(lst):
    for s in lst:
        stack = 0
        for c in s:
            if c == '(':
                stack += 1
            elif c == ')':
                if stack <= 0: 
                    return "No"
                stack -= 1
        if stack > 0:
            return "No"
    return "Yes"