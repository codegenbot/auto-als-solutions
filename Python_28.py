```
strings = []
while True:
    try:
        inp = input("Enter strings separated by space : ")
        if all(s.isalpha() or s.isspace() for s in inp.split()):
            strings = [s.strip() for s in inp.split()]
            break
        else:
            print("Invalid input. Please enter strings only.")
    except ValueError:
        print("Invalid input. Please enter strings only.")

print(' '.join(filter(None, strings)))