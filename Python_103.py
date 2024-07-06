def rounded_avg():
    import math
    n = int(input("Enter the first number: "))
    m = int(input("Enter the second number: "))
    avg = (n + m) / 2
    return bin(int(math.ceil(avg)))[2:]