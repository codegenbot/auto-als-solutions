def add(x: int, y: int) -> int:
    got_valid_input = False

    while not got_valid_input:
        try:
            x = int(input("Enter the first number: "))
            y = int(input("Enter the second number: "))
            got_valid_input = True
            return x + y
        except ValueError:
            print("Invalid input. Please enter a valid integer.")