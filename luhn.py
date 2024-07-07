Here is the Python solution:

def luhn(card_number):
    card_number = [int(x) for x in str(card_number)]
    checksum = sum([num if i % 2 == 0 else num * 2 if num * 2 > 9 else num * 2 - 9 for i, num in enumerate(card_number)])
    return checksum