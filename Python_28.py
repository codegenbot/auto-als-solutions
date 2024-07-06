strings = []
while True:
    try:
        while True:
            inp = input("Enter strings separated by space (or 'stop' to finish): ")
            if inp.lower() == 'stop':
                break
            for s in inp.split():
                if not set(s).issubset({'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '}):
                    raise ValueError
            strings += [s.strip() for s in inp.split()]
        break
    except ValueError:
        print("Invalid input. Please enter strings only.")

print(' '.join(filter(None, strings)))