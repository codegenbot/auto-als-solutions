def decode_shift(s: str):
    key = len(s) - s.count(" ")
    return "".join(
        [
            (
                chr((ord(ch.lower()) - 97 + key) % 26 + 97)
                if ch.isalpha() and ch.islower()
                else chr(ord(ch)) if ch.isalpha() else ch
            )
            for ch in s
        ]
    )