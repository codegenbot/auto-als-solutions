def decode_cyclic():
    s = input("Enter a string: ")
    result = ""
    groups = [s[i : i + 3] for i in range(0, len(s), 3)]
    for group in groups:
        if len(group) == 2:
            result += group[1]
            result += group[0]
        else:
            result += group
    print("Decoded string: ", result)