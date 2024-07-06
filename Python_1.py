for char in paren_string:
    if char == ' ':
        continue
    if char == '(':
        stack.append(char)
        current_group += char
    elif char == ')':
        if stack:
            if stack[-1] == '(':
                stack.pop()
                if not stack:  
                    groups.append(current_group)
                    current_group = ''
            else:
                while stack and stack[-1] != '(':
                    stack.pop()
                if not stack:
                    groups.append(current_group)
                    current_group = ''
        else:
            current_group += char