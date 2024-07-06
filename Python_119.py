Here is the corrected code:

```
def match_parens(lst):
    for string in lst:
        open_count = 0
        close_count = 0
        matching = True
        
        for char in string:
            if char == '(':
                open_count += 1
            elif char == ')':
                if open_count > 0:
                    open_count -= 1
                else:
                    matching = False
        
        if not matching:
            return "No"
    return "Yes"