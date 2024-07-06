```
def get_fibonacci():
    n = int(input("Enter a number: "))
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1 or n == 2:
        print("Fibonacci sequence for", n, "is:", 1)
    else:
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
        print("Fibonacci sequence for", n, "is:", b)