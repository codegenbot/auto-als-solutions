def indices_of_substring(text, target):
    indices = [
        i
        for i in range(len(text) - len(target) + 1)
        if text[i : i + len(target)] == target
    ]
    return indices


if __name__ == "__main__":
    text = input().strip()
    target = input().strip()
    indices = indices_of_substring(text, target)
    print(len(indices))
    if indices:
        print(" ".join(map(str, indices)))