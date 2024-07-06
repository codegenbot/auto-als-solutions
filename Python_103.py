n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))


def rounded_avg(n, m):
    if n == m == 0:
        return "0"
    if n == 0 and m != 0 or n != 0 and m == 0:
        return str(max(abs(n), abs(m)))
    avg = (n + m) / 2
    return bin(int(round(avg)))[2:]


if n != 0 and m != 0:
    print(rounded_avg(n, m))