def sort_even():
    numbers = list(
        map(int, input("Enter even and odd numbers (space separated): ").split())
    )
    print(sorted(numbers))


def check():
    sort_even()