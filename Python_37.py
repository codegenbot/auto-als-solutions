def sort_even():
    even_numbers = list(
        map(int, input("Enter the numbers separated by space: ").split())
    )
    odd_numbers = [i for i in range(1, 100) if i not in even_numbers]
    result = oddEven(even_numbers, odd_numbers)
    print(result)


sort_even()