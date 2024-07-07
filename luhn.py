def luhn(card_num):
    card_num = [int(i) for i in str(card_num)]
    doubled_sum = 0
    for i, num in enumerate(reversed(card_num)):
        if i % 2 == 1:
            num *= 2
            if num > 9:
                num -= 9
        doubled_sum += num
    return str(doubled_sum)