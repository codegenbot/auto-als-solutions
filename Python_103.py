```
n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))

def rounded_avg(n, m):
    if n > m:
        return -1
    avg = round((n + m) / 2)
    return bin(avg)[2:]

print(rounded_avg(n, m))