def check(func):
    result = func()
    if all(num % 2 == 0 for num in result) or all(num % 2 != 0 for num in result):
        print("The output is sorted correctly.")
    else:
        print("The output is not sorted correctly.")

check(sort_even_odd)