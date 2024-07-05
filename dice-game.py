from decimal import Decimal, ROUND_DOWN

def probability_peter_wins(n, m):
    count = 0
    total = n * m
    for p in range(1, n + 1):
        for c in range(1, m + 1):
            if p > c:
                count += 1
    return Decimal(count / total).quantize(Decimal('1.00000000'), rounding=ROUND_DOWN)

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of sides on Peter's die: ").strip())
        m = int(input("Enter the number of sides on Colin's die: ").strip())
        print(probability_peter_wins(n, m))
    except ValueError:
        print("Please enter valid integer values for n and m.")