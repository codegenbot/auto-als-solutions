def indices_of_substring(text):
    target = input()
    result = []
    for i in range(len(text)):
        if text[i:].startswith(target):
            while True:
                index = text[i:i+len(target)].find(target)
                if index == -1:
                    break
                result.append(i + index)
                i += index + len(target)
    return result