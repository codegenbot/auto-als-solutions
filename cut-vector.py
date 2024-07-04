def cut_vector(vector):
    total_sum = sum(vector)
    left_sum = 0
    min_diff = float("inf")
    cut_index = 0

    for i in range(len(vector) - 1):
        left_sum += vector[i]
        right_sum = total_sum - left_sum
        diff = abs(left_sum - right_sum)
        if diff < min_diff:
            min_diff = diff
            cut_index = i + 1

    return vector[:cut_index], vector[cut_index:]

vector = list(map(int, input().strip().split()))
left, right = cut_vector(vector)
print(left)
print(right)