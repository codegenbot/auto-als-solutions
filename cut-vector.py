def cut_vector(lst):
    if len(lst) == 1:
        return [lst], []

    min_diff = float("inf")
    split_index = -1

    for i in range(1, len(lst)):
        diff = abs(sum(lst[:i]) - sum(lst[i:]))
        if diff < min_diff:
            min_diff = diff
            split_index = i

    return lst[: split_index + 1], lst[split_index + 1 :]


print(cut_vector([1]))  # test case for the initial problem statement