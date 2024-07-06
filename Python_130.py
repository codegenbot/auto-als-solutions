def tri(n):
    if n == 0:
        return [3]
    elif n == 1:
        return [3]
    elif n == 2:
        return [3, 2]
    else:
        sequence = [3, 2]
        for i in range(2, n):
            if i % 2 == 0:
                sequence.append(int((i + 1) / 2))
            else:
                last_two = sequence[-2:]
                next_value = sum(last_two)
                sequence.append(next_value)
        return sequence