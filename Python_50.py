def decode_shift(s: str):
    s = s.strip().lower()
    key = len(s) - s.count(' ')
    return "".join([chr((ord(ch)-97+26-key)%26 + 97) if ch.isalpha() and 'a' <= ch <= 'z'
                    else chr(ord(ch)) if ch.isalpha() and not 'a' <= ch <= 'z'
                    else ch for ch in s])

n = int(input("Enter an integer: "))
print(decode_shift(str(n)))