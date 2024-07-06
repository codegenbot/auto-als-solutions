strings = []
while True:
    inp = input("Enter strings separated by space (or 'stop' to finish): ")
    if inp.lower() == 'stop':
        break
    for s in inp.split():
        if set(s).issubset({'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '}):
            strings += [s.strip()]
        else:
            raise ValueError
print(' '.join(filter(None, strings)))