def search(lst):
    frequency_dict = {}
    for num in lst:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    max_freq_num = -1
    for key, value in frequency_dict.items():
        if value > max_freq_num:
            max_freq_num = value
    return max_freq_num