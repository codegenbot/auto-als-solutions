def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    return tuple(sorted((min(numbers), max(numbers)))[:2])