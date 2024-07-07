Here is the solution:

def substitution_cipher(s1, s2, s3):
    result = ""
    for c in s3:
        if c in s1:
            idx = s1.index(c)
            result += s2[idx]
        else:
            result += c
    return result