def match_parens(lst):
    count = 0
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
            count += 1
    return count == len(lst)

num_strings = int(input("Number of strings: "))
input_list = [input("Enter string {}: ".format(i+1)) for i in range(num_strings)]
print(match_parens([s.strip() for s in input_list]))