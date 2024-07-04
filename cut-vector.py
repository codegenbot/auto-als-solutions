def cut_vector(vector):
    if len(vector) == 1:
        return vector, []
    
    total_sum = sum(vector)
    left_sum = 0
    min_diff = float("inf")
    cut_index = -1

    for i in range(len(vector) - 1):
        left_sum += vector[i]
        right_sum = total_sum - left_sum
        diff = abs(left_sum - right_sum)
        if diff < min_diff:
            min_diff = diff
            cut_index = i + 1
        elif diff == min_diff and cut_index == -1:
            cut_index = i + 1 

    return vector[:cut_index], vector[cut_index:]

vector = list(map(int, input().split()))
sub_vect1, sub_vect2 = cut_vector(vector)

print(len(sub_vect1))
print(*sub_vect1)
print(len(sub_vect2))
print(*sub_vect2)