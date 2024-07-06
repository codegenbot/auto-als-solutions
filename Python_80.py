```def is_happy(sentence):
    if len(sentence) < 3:
        return False
    for i in range(0, len(sentence)-2, 3):
        if len(set(sentence[i:i+3])) != 3:
            return False
    return True