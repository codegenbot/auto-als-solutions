```
def mean_absolute_deviation(numbers: List[float]) -> float:
    if len(numbers) == 0:
        return 0
    total = sum(abs(num) for num in numbers)
    count = len(numbers)
    mean = total / count
    
    return sum(abs(num - mean) for num in numbers) / count