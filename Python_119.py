def match_parens(lst):
    open_count = 0
    close_count = 0
    matching = True
    
    for string in lst:
        for char in string:
            if char == '(':
                open_count += 1
            elif char == ')':
                close_count += 1
        
        if open_count != close_count:
            matching = False
            break
        
        open_count = 0
        close_count = 0
    
    return "Matching" if matching else "Not Matching"