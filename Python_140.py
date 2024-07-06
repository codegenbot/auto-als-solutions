def fix_spaces(text):
    new_text = text.replace("   ", "_-").replace("  ", "_-").replace(" ", "_")
    while "___" in new_text:
        new_text = new_text.replace("___", "_-")
    return new_text