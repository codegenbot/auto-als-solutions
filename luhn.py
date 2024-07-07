```
def luhn_sum(card):
    sum = 0
    for i, digit in enumerate(map(int, card)):
        if (i % 2) == 1:
            double_digit = digit * 2
            if double_digit > 9:
                double_digit -= 9
        else:
            double_digit = digit
        sum += double_digit
    return sum