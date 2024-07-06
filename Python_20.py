def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    return tuple(
        sorted(
            (a, b) for a, b in zip(numbers, numbers[1:]) + [(numbers[0], numbers[-1])]
        )[0][::-1]
    )