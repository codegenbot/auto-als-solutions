def rounded_avg():
    n = int(input("Enter the first number: "))
    avg1 = round(n / 2)
    m = int(input("Enter the second number: "))
    avg2 = round(m / 2)
    return bin(int(avg1 + avg2))[2:]