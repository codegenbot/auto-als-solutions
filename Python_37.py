def check(func):
    result = func()
    print(result)

def sort_even_odd():
    even_numbers = input("Enter even numbers (space separated): ")
    odd_numbers = input("Enter odd numbers (space separated): ")

    even = list(map(int, even_numbers.split()))
    odd = list(map(int, odd_numbers.split()))

    even.sort()
    odd.sort()

    return sorted(even + odd)

check(sort_even_odd)