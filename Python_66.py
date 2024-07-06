def digitSum(s):
    return sum(
        ord(c) - 55 if "A" <= c <= "F" else ord(c) - 61 if "a" <= c <= "f" else 0
        for c in s
    )