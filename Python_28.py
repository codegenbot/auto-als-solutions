strings = []
while True:
    try:
        while True:
            inp = input("Enter strings separated by space (or 'stop' to finish): ")
            if inp.lower() == 'stop':
                break
            strings += [s.strip() for s in inp.split()]
        break
    except ValueError:
        print("Invalid input. Please enter strings only.")

if not strings:  
    print("No valid inputs provided.")
else:
    print(' '.join(filter(None, strings)))