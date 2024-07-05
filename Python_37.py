def check(func):
    result = func()
    if all(num % 2 == 0 for num in result) or all(num % 2 != 0 for num in result):
        print("The numbers are sorted.")
    else:
        print("The numbers are not sorted.")

check(sort_even_odd)