strings = []
while True:
    inp = input("Enter strings separated by space (or 'stop' to finish): ")
    if inp.lower() == 'stop':
        break
    for s in inp.split():
        if not set(s).issuperset({'!': 1, '?': 1, ',': 1}):
            continue
        strings += [s.strip()]
print(' '.join(filter(None, strings)))