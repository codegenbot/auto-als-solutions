def tri(n):
    if n == 0:
        return [3]
    elif n == 1:
        return [3]
    elif n == 2:
        return [3, 2]
    else:
        seq = [3, 2]
        for _ in range(2, n):
            next_num = seq[-1] + seq[-2] + (seq[-3] if len(seq) > 2 else 0)
            seq.append(next_num // 2 if len(seq) % 2 == 0 else int(next_num))
        return seq