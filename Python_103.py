def rounded_avg():
    n, m = map(int, input("Enter two numbers: ").split())
    if n > m:
        return -1
    avg = (n + m) // 2
    return f"The average is {avg}"

print(rounded_avg())