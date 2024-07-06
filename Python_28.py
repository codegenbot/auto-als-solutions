strings = []
while True:
    inp = input("Enter strings separated by space (or 'stop' to finish): ")
    if inp.lower() == 'stop':
        break
    for s in inp.split():
        if not set(s).issubset(set('abcdefghijklmnopqrstuvwxyz ')):
            continue
        strings += [s.strip()]
    if not strings:  
        print("No input received. Please enter some strings.")
        continue
print(' '.join(filter(None, strings)))