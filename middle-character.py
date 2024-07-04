def middle_character(s):
    length = len(s)
    if length % 2 == 0:
        return s[(length // 2) - 1 : (length // 2) + 1]
    else:
        return s[length // 2]


# Reading input
s = input().strip()
print(middle_character(s))