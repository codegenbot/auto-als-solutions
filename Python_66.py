def digitSum(s):
    return sum(int(c) if c.isdigit() else ord(c) - 55 for c in s)