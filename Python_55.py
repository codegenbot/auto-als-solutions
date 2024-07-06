def print_fibonacci():
    n = int(input("Enter a number: "))
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1 or n == 2:
        print("Fibonacci sequence up to", n, ":", 1)
    else:
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
        print("Fibonacci sequence up to", n, ":", 1, end=" ")
        while a <= n:
            print(a, end=" ")
            a, b = b, a + b
        print()