```
def find_fibonacci():
    n = int(input("Enter a positive integer: "))
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1 or n == 2:
        print(f"Fibonacci number at position {n} is 1")
    else:
        fib_num = [1, 1]
        for i in range(2, n):
            fib_num.append(fib_num[i-1] + fib_num[i-2])
        print(f"Fibonacci number at position {n} is {fib_num[-1]}")