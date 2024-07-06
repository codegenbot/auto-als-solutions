```
def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0:
        return False
    last_char = txt[-1]
    if not last_char.isalpha():
        return True
    for i in range(len(txt)-2, -1, -1):
        if not txt[i].isspace() and not txt[i].isalpha():
            break
    else:
        return False
    return True