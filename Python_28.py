```
strings = []
while True:
    inp = input("Enter strings separated by space (or 'stop' to finish): ")
    if inp.lower() == 'stop':
        break
    for s in inp.split():
        try:
            s = ''.join(filter(str.isalpha, s)).lower()
            strings.append(s)
        except Exception as e:
            print(f"Error: {e}. Please enter valid string.")
print(' '.join(filter(None, strings)))