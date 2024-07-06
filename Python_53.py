```
def add(x: int, y: int) -> int:
    while True:
        while True:
            try:
                x = int(input("Enter the first number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        while True:
            try:
                y = int(input("Enter the second number: "))
                return x + y
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")