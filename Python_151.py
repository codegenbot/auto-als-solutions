def check(lst, double_the_difference):
    print(double_the_difference([i**2 for i in lst if isinstance(i, int) and i >= 0]))