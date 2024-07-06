```
def match_parens(lst):
    for s in lst:
        open_count = 0
        close_count = 0
        for char in s:
            if char == '(':
                open_count += 1
            elif char == ')':
                close_count += 1
                if open_count < close_count:
                    break
        if open_count == close_count:
            return "Strings have matching parentheses"
    return "Strings do not have matching parentheses"

input_list = [s.strip() for s in (input("Enter string {}: ".format(i+1)) for i in range(int(input("Number of strings: "))))]
print(match_parens(input_list))