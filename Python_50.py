```Python
n = input("Enter a string: ")
if n.isalnum():
    print(decode_shift(n))
else:
    print("Invalid input. Please enter only alphanumeric characters and spaces.")