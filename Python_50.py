def decode_shift():
    s = input("Enter the encoded text: ")
    if isinstance(s, str):
        return "".join([chr(((ord(ch) - 97 if ch.islower() else 65) - 5) % 26 + 97 if ch.islower() else 65) for ch in s])
    else:
        return "Invalid input. Please enter a string."