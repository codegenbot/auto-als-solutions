```
def decode_shift(s: str):
    s = s.strip().lower()
    key = len(s) - s.count(' ')
    
    decoded_str = ""
    shift = 0
    for ch in s:
        if not ch.isalpha():
            decoded_str += ch
            shift = 1
        elif 'a' <= ch <= 'z':
            if shift:
                if ord(ch)-97+key <= 26:
                    decoded_str += chr((ord(ch)-97+key)%26 + 97)
                else:
                    decoded_str += chr(96+(ord(ch)-97+key)%26) 
                shift = 0
            else:
                decoded_str += ch
        elif 'A' <= ch <= 'Z':
            if shift:
                if ord(ch)-65+key <= 26:
                    decoded_str += chr((ord(ch)-65+key)%26 + 65)
                else:
                    decoded_str += chr(90+(ord(ch)-65+key)%26) 
                shift = 0
            else:
                decoded_str += ch
        else: 
            decoded_str += ch
    
    return decoded_str

n = input("Enter a string: ")
print(decode_shift(n))