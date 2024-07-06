def solve(N):
    if not isinstance(N, int):
        return "Error: Input must be an integer"
    total = 0
    temp = N
    while temp > 0:
        last_digit = temp % 10
        if last_digit == 1:
            total += 2 ** (len(str(N)) - 1)
        elif last_digit == 3:
            total += 2 ** (len(str(N)) - 1) * 3
        else:
            total += int('1' + '0' * (len(str(N)) - 1) + str(last_digit), 2)
        temp //= 10
    return total