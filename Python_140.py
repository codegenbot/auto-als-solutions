```
def fix_spaces(text):
    result = ''
    prev_space = False
    for char in text:
        if char.isspace():
            if prev_space:
                result += '-'
            else:
                result += '_'
            prev_space = True
        else:
            result += char
            prev_space = False
    return result