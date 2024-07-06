def tri(n):
    if n == 0:
        return [3]
    elif n == 1:
        return [3]
    elif n == 2:
        return [3, 2]
    else:
        tribonacci_sequence = [3, 2]
        for i in range(2, n):
            if i % 2 == 0:
                tribonacci_sequence.append(1 + i / 2)
            else:
                a, b = tribonacci_sequence[-2], tribonacci_sequence[-3]
                tribonacci_sequence.append(
                    a + b + (tribonacci_sequence[0] if i > 0 else 3)
                )
        return tribonacci_sequence