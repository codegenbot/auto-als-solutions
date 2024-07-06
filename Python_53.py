def add(x: int, y: int) -> int:
    while True:
        try:
            x = int(input("Enter the first number: "))
            y = int(input("Enter the second number: "))
            print(f"The sum of {x} and {y} is: {x + y}")
            cont = input("Do you want to add again? (yes/no): ")
            if cont.lower() != 'yes':
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")