def bouncing_balls():
    h1 = float(input())
    h2 = float(input())
    n = int(input())

    bounciness_index = h2 / h1
    total_distance = (n * 2) + ((n * 2) - 1) * (h2 / h1)

    return "%.6f\n" % total_distance


print(bouncing_balls())