def binary_average(n1, n2):
    if n1 < 0 or n2 < 0:
        return "Error: Numbers should be non-negative."
    elif n1 > n2:
        return -1
    else:
        total = n1 + n2
        avg = round(total / 2)
        binary_avg = bin(avg)[2:]
        return binary_avg