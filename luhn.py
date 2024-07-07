def luhn(card_number):
    sum = 0
    for i in range(15, -1, -1):
        if i % 2 != 0:
            double_card = int(str(card_number)[i]) * 2
            if double_card > 9:
                sum += double_card - 9
            else:
                sum += double_card
        else:
            sum += int(str(card_number)[i])
    return sum