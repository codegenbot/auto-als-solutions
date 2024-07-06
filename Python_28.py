strings = []
while True:
    try:
        inp = input("Enter strings separated by space : ")
        strings = [s.strip() for s in inp.split()]
        break
    except ValueError:
        print("Invalid input. Please enter strings only.")
        strings.clear()

print(' '.join(map(str, filter(None, strings))))