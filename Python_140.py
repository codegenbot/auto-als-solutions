```
def fix_spaces(text):
    text += " "
    new_text = ""
    for char in text:
        if char != " " or new_text[-1] != " ":
            new_text += char
        elif new_text and new_text[-1] != "-":
            new_text += "-"
        else:
            new_text += " "
    return new_text.strip()