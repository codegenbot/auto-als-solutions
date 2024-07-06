import hashlib


def string_to_md5(text):
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()


def check_password():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        hashed_input = string_to_md5(password)

        valid_usernames = ["admin", "john"]
        valid_passwords = ["password123", hashlib.md5(b"password123").hexdigest()]

        if username in valid_usernames and hashed_input in valid_passwords:
            print("Access granted!")
            break
        else:
            print("Invalid username or password. Try again!")


check_password()