def match_parens(lst):
    stack = 0
    res = 0
    for s in lst:
        stack = 0
        for c in s:
            if c == '(':
                stack += 1
            elif c == ')':
                if stack > 0:
                    stack -= 1
                else:
                    res += 1
        res += stack * 2
    return res

input_list = [input("Enter string {}: ".format(i+1)) for i in range(int(input("Number of strings: ")))]
print(match_parens([s.strip() for s in input_list]))