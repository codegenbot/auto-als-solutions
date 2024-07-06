```
def add(x: int, y: int) -> int:
    while True:
        try:
            while True:
                x = int(input("Enter the first number: "))
                if type(x) == int:
                    break
            while True:
                y = int(input("Enter the second number: "))
                if type(y) == int:
                    break
            return x + y
        except ValueError:
            print("Invalid input. Please enter a valid integer.")