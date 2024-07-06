def rounded_avg():
    n = int(input("Enter the first number: "))
    avg1 = round(n / 1)
    m = int(input("Enter the second number: "))
    avg2 = round(m / 1)
    total_avg = (avg1 + avg2) / 2
    return bin(int(total_avg))[2:]

print(rounded_avg())