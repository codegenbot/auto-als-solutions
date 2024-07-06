def add(x: int, y: int) -> int:
    while True:
        try:
            x = int(input("Enter the first number: "))
            if x != 0:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        try:
            y = int(input("Enter the second number: "))
            if y != 0:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    return x + y