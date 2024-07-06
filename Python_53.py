```python
def add(x: int, y: int) -> int:
    while True:
        try:
            while True:
                x = input("Enter the first number: ")
                if x.replace('-', '',).replace('.', '',).isdecimal():
                    x = int(x)
                    break
                print("Invalid input. Please enter a valid integer.")
                
            while True:
                y = input("Enter the second number: ")
                if y.replace('-', '',).replace('.', '',).isdecimal():
                    y = int(y)
                    break
                print("Invalid input. Please enter a valid integer.")
            
            print(f"The sum of {x} and {y} is: {x + y}")
            cont = input("Do you want to add again? (yes/no): ")
            if cont.lower() != 'yes':
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")