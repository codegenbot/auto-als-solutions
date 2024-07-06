```
n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))

def rounded_avg(n, m):
    if isinstance(n, int) and isinstance(m, int):
        avg = (n + m) / 2
        return bin(int(round(avg)))[2:]
    else:
        return "Invalid input. Please enter integers."