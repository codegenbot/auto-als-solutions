def substitution_cipher(cipher1, cipher2, message):
    return "".join(
        [cipher2[i] if i < len(cipher2) else "" for i in range(len(message))]
    )


# test cases
print(substitution_cipher("a", "z", "a"))  # z
print(substitution_cipher("j", "h", "jj"))  # hh
print(substitution_cipher("a", "z", "azza"))  # zzazz
print(substitution_cipher("e", "l", "eeeeeeeeee"))  # llllllllll