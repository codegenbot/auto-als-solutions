def check(lst, double_the_difference):
    print(double_the_difference([i for i in lst if isinstance(i, int) and i >= 0]))