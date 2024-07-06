def decode_shift(s: str):
    s = s.strip().lower()
    key = len(s) - s.count(" ")
    return "".join(
        [
            (
                chr((ord("a") + (ord(ch.lower()) - ord("a")) + 26 - key) % 26)
                if ch.isalpha()
                else chr(ord(ch))
            )
            for ch in s
        ]
    )