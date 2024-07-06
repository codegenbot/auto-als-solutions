def sum_product(numbers: List[int]) -> Tuple[int, int]:
    total_sum = 0
    product = 1
    
    for num in numbers:
        if num == 0:
            return (0, 1)
        total_sum += num
        product *= num
    
    return (total_sum, product)