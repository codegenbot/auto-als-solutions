def match_parens(lst):
    stack = []
    for s in lst:
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if len(stack) == 0:
                    return 'No'
                stack.pop()
    if len(stack) == 0:
        return 'Yes'
    else:
        return 'No'

input_list = input("Enter your string: ")
print(match_parens(input_list))