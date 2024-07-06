```Python
def add(x: int, y: int) -> int:
    while True:
        try:
            x = int(input("Enter the first number: "))
            if x == -1:  
                return None 
            while True:
                try:
                    y = int(input("Enter the second number: "))
                    if y == -1:  
                        return None  
                    return x + y
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")