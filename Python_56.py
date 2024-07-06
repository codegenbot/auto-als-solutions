```
def correct_bracketing(s: str) -> bool:
    open_brackets = set(['(', '[', '<'])
    close_brackets = {')': '(', ']': '[', '>': '<'}
    stack = []
    
    for char in s:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if not stack or close_brackets[char] != stack.pop():
                return False
    
    return not stack