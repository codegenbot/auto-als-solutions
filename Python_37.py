```
def sort_even(l: list):
    even_nums = [i for i in l if i % 2 == 0]
    odd_nums = [j for j in l if j % 2 != 0]
    return sorted(even_nums) + odd_nums