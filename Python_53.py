```
def add(x: int, y: int) -> int:
    got_valid_input = False

    while not got_valid_input:
        try:
            x = int(input("Enter the first number: "))
            got_valid_input = True
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    got_second_valid_input = False
    while not got_second_valid_input:
        try:
            y = int(input("Enter the second number: "))
            got_second_valid_input = True
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    return x + y