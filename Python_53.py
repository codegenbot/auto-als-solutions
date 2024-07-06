```
def add(x: int, y: int) -> int:
    while True:
        try:
            x = int(input("Enter the first number: "))
            y = int(input("Enter the second number: "))
            print(f"Result: {x + y}")
            cont = input("Do you want to continue? (yes/no): ")
            if cont.lower() != "yes":
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")