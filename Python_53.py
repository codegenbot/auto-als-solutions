```
def add(x: int, y: int) -> int:
    while True:
        try:
            x = int(input("Enter the first number: "))
            if isinstance(y, (int)):
                break
            y = int(input("Enter the second number: "))
            return x + y
        except ValueError:
            print("Invalid input. Please enter a valid integer.")