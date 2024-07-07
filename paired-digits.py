def paired_digits(digits):
    return sum(
        int(digit)
        for i, digit in enumerate(str(digits))
        if i < len(str(digits)) - 1 and int(digit) == int(str(digits)[i + 1])
    )