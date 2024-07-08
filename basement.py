```
def basement(arr):
    total_sum = 0
    indices = [0]
    for i in range(len(arr)):
        total_sum += arr[i]
        if total_sum < 0:
            return i + 1
        elif total_sum > 0 and (len(indices) == 1 or total_sum != indices[-1]):
            indices.append(total_sum)
    return -1