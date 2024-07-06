def double_the_difference(lst):
    even_sum = sum(i for i in lst if isinstance(i, int) and i % 2 == 0)
    odd_sum = sum(i for i in lst if isinstance(i, int) and i % 2 != 0)

    return (
        abs(sum(i**2 for i in lst if isinstance(i, int)) - (2 * even_sum))
        if odd_sum == 0
        else abs(even_sum - (2 * odd_sum))
    )


input_list = [1, 2, 3, 4]
print(double_the_difference(input_list))