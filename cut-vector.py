def cut_vector(lst):
    for i in range(len(lst) - 1):
        if np.abs(np.mean(lst[: i + 1]) - np.mean(lst[i:])).argmin() == 0:
            return [lst[: i + 1], lst[i:]]
    return [lst, []]