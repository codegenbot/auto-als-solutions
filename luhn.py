```
def luhn(card):
    card = list(map(int, card))
    total = 0
    for i, digit in enumerate(reversed(card)):
        if i % 2 == 0:
            if i == 0:  
                digit *= 2
            else:
                digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    return total