def rounded_avg(n, m):
    avg = (n + m) / 2
    return bin(int(round(avg)))[2:]


k = int(input("Enter the first number for function: "))
p = int(input("Enter the second number for function: "))

n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))

print(rounded_avg(k, p))