n = float(input("Enter the first number: "))
m = float(input("Enter the second number: "))

def rounded_avg(n, m):
    avg = (n + m) / 2
    if not avg.is_integer():
        return str(int(round(avg)))
    return bin(int(round(avg)))[2:]