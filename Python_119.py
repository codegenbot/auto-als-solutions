def match_parens(lst):
    open_parens = 0
    close_parens = 0
    
    for s in lst:
        if s[0] == '(':
            open_parens += 1
        elif s[0] == ')':
            if open_parens > 0:
                open_parens -= 1
            else:
                return 'No'  
                
    return 'Yes' if open_parens == 0 and close_parens == 0 else 'No'