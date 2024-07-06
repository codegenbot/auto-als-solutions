```
def decode_shift(s: str):
    s = s.strip().lower()
    key = len(s) - s.count(' ')
    
    decoded_str = ""
    shift = 0
    for ch in s:
        if not ch.isalpha():
            decoded_str += ch
        elif 'a' <= ch <= 'z':
            if shift:
                decoded_str += chr((ord(ch)-97+26-key)%26 + 97)
            else:
                decoded_str += chr(ord(ch))
            shift = 0
        else: 
            decoded_str += ch
    
    return decoded_str

n = input("Enter a string: ")
print(decode_shift(n))