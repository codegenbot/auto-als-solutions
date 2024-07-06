```
def search(lst):
    frequency_dict = {}
    for num in lst:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    max_freq_num = -1
    max_freq_count = 0
    for key, value in frequency_dict.items():
        if value > max_freq_count:
            max_freq_num = key
            max_freq_count = value
    return max_freq_num