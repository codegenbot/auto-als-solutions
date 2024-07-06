def add(x: int, y: int) -> int:
    while True:
        try:
            x = int(input("Enter the first number: "))
            y = int(input("Enter the second number: "))
            if input("Do you want to add another pair? (yes/no): ").lower() != 'no':
                return x + y
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")