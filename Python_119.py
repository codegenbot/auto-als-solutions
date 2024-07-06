input_list = [
    input("Enter string {}: ".format(i + 1))
    for i in range(int(input("Number of strings: ")))
]
print(match_parens([s.strip() for s in input_list]))