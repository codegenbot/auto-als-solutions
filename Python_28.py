strings = []
while True:
    inp = input("Enter strings separated by space (or 'stop' to finish): ")
    if inp.lower() == 'stop':
        break
    for s in inp.split():
        while len(s) > 1 and not set(s).issubset({'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '}):
            s = input("Invalid string. Please enter a single alphabet character (or 'stop' to finish): ")
            if s.lower() == 'stop':
                break
        strings += [s.strip()]
print(' '.join(filter(None, strings)))