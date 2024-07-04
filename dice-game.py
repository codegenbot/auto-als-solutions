from decimal import Decimal, getcontext

def probability_peter_wins(n, m):
    getcontext().prec = 10
    count = 0
    total = Decimal(n * m)
    for p in range(1, n + 1):
        for c in range(1, m + 1):
            if p > c:
                count += 1
    return round(Decimal(count) / total, 8)

if __name__ == "__main__":
    n = int(input().strip())
    m = int(input().strip())
    print(probability_peter_wins(n, m))