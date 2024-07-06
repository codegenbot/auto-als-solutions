def match_parens(lst):
    for s in lst:
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                stack.pop()
        return not stack
input_list = [input("Enter string {}: ".format(i+1)) for i in range(int(input("Number of strings: ")))]
print(match_parens([s.strip() for s in input_list]))