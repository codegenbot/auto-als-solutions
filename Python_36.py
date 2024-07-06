def fizz_buzz(n: int):
    count = 0
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            count += str(i).count('7')
    return count