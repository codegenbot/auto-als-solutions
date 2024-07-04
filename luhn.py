def luhn_algorithm():
    n = int(input())
    digits = list(map(int, input().split()))
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    print(sum(digits))

luhn_algorithm()