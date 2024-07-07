def unique_numbers() -> List[int]:
    user_input = input("Enter numbers separated by space: ")
    
    if not user_input:
        return []
    
    numbers = list(map(int, user_input.split()))
    return sorted(list(set(numbers)))