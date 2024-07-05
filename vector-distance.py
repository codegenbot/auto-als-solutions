import math


def euclidean_distance():
    n1 = int(input().strip())
    vector1 = list(map(float, input().strip().split()))
    n2 = int(input().strip())
    vector2 = list(map(float, input().strip().split()))

    distance = math.sqrt(sum((v1 - v2) ** 2 for v1, v2 in zip(vector1, vector2)))
    print(distance)


euclidean_distance()