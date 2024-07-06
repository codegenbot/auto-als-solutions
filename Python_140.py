def fix_spaces(text):
    text += " "
    new_text = ""
    for char in text:
        if char != " " or (len(new_text) > 0 and new_text[-1] != " "):
            new_text += char
        elif len(new_text) > 1 and new_text[-1] != "-":
            new_text += "-"
        else:
            new_text += char
    return new_text.strip()