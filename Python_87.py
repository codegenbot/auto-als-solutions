Here is the completed code:

def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        if x in row:
            indices = [j for j, v in enumerate(row) if v == x]
            for index in sorted(indices, reverse=True):
                result.append((i, index))
    return result