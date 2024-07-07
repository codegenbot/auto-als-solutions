def middle_character(s):
    return s[len(s)//2-1 if len(s)%2 else :len(s)//2]