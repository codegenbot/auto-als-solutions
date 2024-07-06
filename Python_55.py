def find_fibonacci():
    n = int(input("Enter a number: "))
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1 or n == 2:
        print("The Fibonacci sequence for", n, "is", 1)
    else:
        a, b = 1, 1
        fib_sequence = [1]
        while len(fib_sequence) < n:
            a, b = b, a + b
            fib_sequence.append(a)
        print("The Fibonacci sequence for", n, "is", fib_sequence)