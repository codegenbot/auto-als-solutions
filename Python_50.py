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
                decoded_str += chr((ord(ch)-97+26-key)%26 + 97) if ch <= 'm' else chr((ord(ch)-101+26-key)%26 + 101)
            else:
                decoded_str += chr(ord(ch))
            shift = 0
        elif 'A' <= ch <= 'Z':
            if shift:
                decoded_str += chr((ord(ch)-65+26-key)%26 + 65) if ch <= 'M' else chr((ord(ch)-69+26-key)%26 + 69)
            else:
                decoded_str += chr(ord(ch))
            shift = 0
        else: 
            decoded_str += ch
    
    return decoded_str

n = input("Enter a string: ")
print(decode_shift(n))