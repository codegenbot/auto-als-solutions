def check(func):
    return func()

def sort_even_odd():
    even_numbers = input("Enter even numbers (space separated): ")
    odd_numbers = input("Enter odd numbers (space separated): ")

    even = list(map(int, even_numbers.split()))
    odd = list(map(int, odd_numbers.split()))

    try:
        even.sort()
        odd.sort()
        return sorted(even + odd)
    except ValueError as e:
        print(f"Error: {str(e)}")
        return None

check(sort_even_odd())