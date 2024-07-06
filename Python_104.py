def unique_digits(x):
    return sorted(
        [i for i in range(1, x + 1) if not any(int(digit) % 2 == 0 for digit in str(i))]
    )