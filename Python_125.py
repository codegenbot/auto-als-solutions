def split_words(txt):
    return (
        txt.split()
        if any(char in txt for char in " ")
        else txt.replace(",", " ").split()
    )