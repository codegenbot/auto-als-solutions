```
def tri(n):
    if n == 0:
        return [3]
    elif n == 1:
        return [1, 3]
    else:
        sequence = [1, 3]
        for i in range(2, n + 1):
            if i % 2 == 0:
                sequence.append(int(i / 2) + (sequence[i-1] if i > 1 else 0))
            else:
                sequence.append(sequence[i-1] + sequence[i-2] + sequence[i+1])
        return sequence