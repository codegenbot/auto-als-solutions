def rounded_avg():
    from math import ceil
    n = int(input("Enter the first number: "))
    m = int(input("Enter the second number: "))
    avg = (n + m) / 2
    return bin(int(ceil(avg)))[2:]