n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))


def rounded_avg(n, m):
    if n == 0 and m != 0:
        return "1"
    elif n != 0 and m == 0:
        return "1"
    elif n == 0 and m == 0:
        return "0"
    avg = (n + m) / 2
    return bin(int(round(avg)))[2:]


print(rounded_avg(n, m))