while True:
    observations = [float(input()) for _ in range(47)]
    if observations[28] > 0.5:
        print(28)
    elif observations[29] > 0.5:
        print(29)
    elif observations[30] > 0.5:
        print(30)
    elif observations[31] > 0.5:
        print(31)
    elif observations[32] > 0.5:
        print(32)
    elif observations[33] > 0.5:
        print(33)
    else:
        print(0)