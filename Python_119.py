def match_parens(lst):
    for string in lst:
        open_count = 0
        close_count = 0
        matching = True
        
        for char in string:
            if char == '(':
                open_count += 1
                close_count = 0  # reset the count of closing parentheses
            elif char == ')':
                close_count += 1
                if close_count > open_count:  # check if they are matched correctly
                    matching = False
                    break
        
        if not matching:
            return "No"
    return "Yes"