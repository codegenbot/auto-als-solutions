```
def fix_spaces(text):
    text += ' '
    new_text = ''
    count = 0
    for char in text:
        if char == ' ' and count < 2:
            new_text += '_'
            count = 0
        elif char != ' ':
            new_text += char
            count = 0
        else:
            count += 1
            new_text += '-'
    return new_text.rstrip()