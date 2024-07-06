```
def tri(n):
    if n == 0:
        return [3]
    elif n == 1:
        return [3, 1]
    else:
        sequence = [3, 1]
        for _ in range(2, n + 1):
            if _ % 2 == 0:
                sequence.append(1 + _ // 2)
            else:
                a, b = sequence[-2], sequence[-1]
                sequence.append(a + b + (sequence[0] if _ > 0 else 3))
        return sequence