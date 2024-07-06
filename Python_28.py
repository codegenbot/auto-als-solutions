```
strings = []
while True:
    try:
        inp = input("Enter strings separated by space : ")
        strings = [s.strip() for s in inp.split()]
        break
    except ValueError:
        print("Invalid input. Please enter strings only.")

print(' '.join(filter(None, strings)))