def paired_digits(s):
    return sum(int(digit) for digit, nxt in zip(s, s[1:]) if digit == nxt)