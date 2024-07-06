def fix_spaces(text):
    new_text = text.replace(" ", "_")
    while "__" in new_text:
        new_text = new_text.replace("__", "_")
    new_text = (
        new_text.replace("_+_", "_-").replace("_++_", "_-").replace("_+++_", "_-")
    )
    return new_text