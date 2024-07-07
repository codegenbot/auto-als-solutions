def indices_of_substring(text):
    result = []
    start = 0
    while start < len(text):
        pos = text.find(target, start)
        if pos == -1:
            break
        result.append(pos)
        start = pos + 1
    return result


text = input()
target = int(input())
print(indices_of_substring(text))