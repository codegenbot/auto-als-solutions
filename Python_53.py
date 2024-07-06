def add(x: int, y: int) -> int:
    while True:
        try:
            x = int(input("Enter the first number: "))
            if not x:
                print("Please enter a valid integer.")
                continue
            y = int(input("Enter the second number: "))
            if not y:
                print("Please enter a valid integer.")
                continue
            return x + y
        except ValueError:
            print("Invalid input. Please enter a valid integer.")