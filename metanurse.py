while True:
    observations = [float(input()) for _ in range(47)]
    action = 0
    if observations[28] > 0:
        action = 28
    elif observations[29] > 0:
        action = 29
    elif observations[30] > 0:
        action = 30
    elif observations[31] > 0:
        action = 31
    elif observations[32] > 0:
        action = 32
    elif observations[33] > 0:
        action = 33
    elif observations[34] > 0:
        action = 34
    elif observations[35] > 0:
        action = 35
    else:
        action = 36
    print(action)