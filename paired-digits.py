def paired_digits(s):
    return sum(int(digit) for i, digit in enumerate(s + s[0]) if digit == s[i+1])