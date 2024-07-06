```Python
n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))

def rounded_avg(n, m):
    avg = (n + m) / 2
    return bin(int(round(avg)))[2:]

print(rounded_avg(n, m))