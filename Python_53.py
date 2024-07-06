```
def add(x: int, y: int) -> int:
    cont = input("Do you want to add numbers? (yes/no): ")
    while cont.lower() == 'yes':
        try:
            x = int(input("Enter the first number: "))
            y = int(input("Enter the second number: "))
            print(f"The sum of {x} and {y} is: {x + y}")
            cont = input("Do you want to add again? (yes/no): ")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    print("Goodbye!")