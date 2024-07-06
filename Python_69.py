```
def search(lst):
    frequency = {}
    for num in lst:
        if num > 0:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
    max_num = -1
    for key, value in frequency.items():
        if value >= key and key > 0:
            max_num = key
    return max_num