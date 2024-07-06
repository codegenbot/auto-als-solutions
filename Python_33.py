```
def sort_third(l: list):
    nums_divisible_by_3 = [i for i in l if i % 3 == 0]
    sorted_divisible_by_3 = sorted([x for x in l if x % 3 == 0])
    result = []
    i = j = 0
    for num in l:
        if num % 3 != 0:
            result.append(num)
        else:
            if i < len(nums_divisible_by_3):
                result.append(sorted_divisible_by_3[j])
                j += 1
                i += 1
    return result