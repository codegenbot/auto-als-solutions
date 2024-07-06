def fix_spaces(text):
    text = text.replace(" ", "_")
    return (
        text.replace(" " + "_" * 100 + " ", "-")
        .replace("_", "_ ")
        .strip()
        .replace("   ", " - ")
        .replace("- ", " _- ")
        .replace("-", "_- ")
        .strip()
    )