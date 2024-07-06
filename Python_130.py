def tri(n):
    if n == 0:
        return [3]
    elif n == 1:
        return [3]
    elif n == 2:
        return [3, 2]
    else:
        result = [3, 2]
        for i in range(2, n):
            if i % 2 == 0:
                result.append(1 + i / 2)
            else:
                last_three = result[-3:]
                result.append(sum(last_three))
        return result