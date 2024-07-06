def add(x: int, y: int) -> int:
    while True:
        try:
            x = int(input("Enter the first number: "))
            if type(x) != int:
                print("Invalid input. Please enter a valid integer.")
                continue
            y = int(input("Enter the second number: "))
            if type(y) != int:
                print("Invalid input. Please enter a valid integer.")
                continue
            return x + y
        except ValueError:
            print("Invalid input. Please enter a valid integer.")