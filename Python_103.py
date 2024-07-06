n = None
m = None

while True:
    try:
        n = int(input("Enter the first number: "))
        m = int(input("Enter the second number: "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


def rounded_avg(n, m):
    avg = (n + m) / 2
    return bin(int(round(avg)))[2:]


print(rounded_avg(n, m))