def sort_third(l: list):
    third_nums = [x for x in l if x % 3 == 0]
    sorted_third = sorted(third_nums)
    result = []
    third_index = 0
    for num in l:
        if num % 3 != 0:
            result.append(num)
        else:
            if len(sorted_third) > third_index:
                result.append(sorted_third[third_index])
                third_index += 1
            else:
                result.append(num)
    return result