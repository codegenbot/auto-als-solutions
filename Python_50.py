def decode_shift(s: str):
    s = s.strip().lower()
    key = len(s) - s.count(' ')
    
    decoded_str = ""
    for char in s:
        if char.isalpha():
            if 'a' <= char <= 'z':
                decoded_str += chr((ord(char)-97+26-key)%26 + 97)
            else:
                decoded_str += chr(ord(char))
        else:
            decoded_str += char
    
    return decoded_str

n = input("Enter a string: ")
print(decode_shift(n))