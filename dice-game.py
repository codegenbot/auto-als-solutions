def probability_peter_wins(n, m):
    count = 0
    total = n * m
    for p in range(1, n + 1):
        for c in range(1, m + 1):
            if p > c:
                count += 1
    return count / total

if __name__ == "__main__":
    n = int(input().strip())
    m = int(input().strip())
    print(f"{probability_peter_wins(n, m):.8f}")