```
import hashlib

def string_to_md5():
    while True:
        text = input("Enter a string: ")
        if not text:
            print("No input provided. Please try again.")
        else:
            return hashlib.md5(text.encode()).hexdigest()

print(string_to_md5())