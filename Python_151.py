def double_the_difference(lst):
    odd_sum = sum(i for i in lst if i % 2 != 0)
    return (
        sum(i**2 for i in lst if isinstance(i, int) and i >= 0 and i % 2 != 0) / odd_sum
    )


def check():
    lst = [1, -2, 3, 4, 5]
    assert round(double_the_difference(lst), 2) == 4.0


check()