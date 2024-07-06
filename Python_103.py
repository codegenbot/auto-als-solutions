```
n = int(input("Enter number n: "))
m = int(input("Enter number m: "))
def rounded_avg(n, m):
    if n > m:
        return -1
    avg = round((n + m) / 2)
    return bin(avg)[2:]