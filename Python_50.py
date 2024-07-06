def decode_shift(s: str):
    return "".join(
        [
            chr(
                (ord(ch) - 3 if "n" <= ch <= "z" else ord(ch) - 3 + 26) % 26 + 97
                if ch.islower()
                else ord(ch) - 32
            )
            for ch in s
        ]
    )