def luhn(card_number):
    card_number = list(map(int, str(card_number)))
    total_sum = 0
    for i in range(len(card_number) - 1):
        if (i) % 2 == 0:
            card_number[i] *= 2
            if card_number[i] > 9:
                card_number[i] -= 9
        total_sum += card_number[i]
    return total_sum + card_number[-1]


print(luhn(0))
for _ in range(int(input(""))):
    card_number = list(map(int, input().split()))
    print(luhn(sum(card_number)))