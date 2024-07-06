def fix_spaces(text):
    new_text = text.replace(" ", "_")
    while "__" in new_text:
        new_text = new_text.replace("__", "_")
    new_text = (
        new_text.replace("_- -", "-").replace("_-   ", "-").replace("_-    ", "-")
    )
    return new_text