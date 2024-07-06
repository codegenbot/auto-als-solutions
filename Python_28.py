```
from typing import List


def concatenate():
    while True:
        try:
            strings = input("Enter space-separated strings (or 'stop' to finish): ").split()
            if strings[0].lower() == 'stop':
                break
            return " ".join(strings)
        except ValueError:
            print("Invalid input. Please enter a list of strings.")

print(concatenate())