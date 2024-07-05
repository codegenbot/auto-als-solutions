```
def check(func):
    result = func()
    return result

def sort_even_odd():
    even_numbers = input("Enter even numbers (space separated): ")
    odd_numbers = input("Enter odd numbers (space separated): ")

    try:
        even = list(map(int, even_numbers.split()))
        odd = list(map(int, odd_numbers.split()))

        if not all(num % 2 == 0 for num in even):
            raise ValueError("Invalid even numbers")
        if not all(num % 2 != 0 for num in odd):
            raise ValueError("Invalid odd numbers")

        even.sort()
        odd.sort()

        return sorted(even + odd)
    except ValueError as e:
        print(e)
        return None

check(sort_even_odd())