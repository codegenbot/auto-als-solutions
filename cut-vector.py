def cut_vector(vec):
    total_sum = sum(vec)
    left_sum = 0
    min_diff = float("inf")
    cut_index = 0

    for i in range(len(vec) - 1):
        left_sum += vec[i]
        right_sum = total_sum - left_sum
        diff = abs(left_sum - right_sum)
        if diff < min_diff:
            min_diff = diff
            cut_index = i + 1

    return vec[:cut_index], vec[cut_index:]


# Reading input
vec = list(map(int, input().split()))
left, right = cut_vector(vec)
print(left)
print(right)