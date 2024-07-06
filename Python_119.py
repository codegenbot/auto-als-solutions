def match_parens(lst):
    """Complete the following code given the task description and function signature.."""
    for string in lst:
        open_count = 0
        close_count = 0
        matching = True
        
        for char in string:
            if char == '(':
                open_count += 1
            elif char == ')':
                close_count += 1
        
        if open_count != close_count:
            matching = False
        
        if not matching:
            return "No"
    return "Yes"