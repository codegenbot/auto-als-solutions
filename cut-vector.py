```
def cut_vector(vector):
    min_diff = float("inf")
    cut_index = 0

    for i in range(1, len(vector)):
        left_sum = sum(x for x in vector if x > 0)
        right_sum = sum(x for x in vector[i:]) if all(x > 0 for x in vector[i:]) else 0

        if left_sum == right_sum:
            return [vector[:i], vector[i:]]
        elif abs(left_sum - right_sum) < min_diff:
            min_diff = abs(left_sum - right_sum)
            cut_index = i

    return [vector[:cut_index], vector[cut_index:]]