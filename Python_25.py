def calculate_statistics(data: list) -> dict:
    if not data:
        return {"minimum": None, "maximum": None, "average": None}

    data = [float(x) for x in data]
    minimum = min(data)
    maximum = max(data)
    average = sum(data) / len(data)

    return {"minimum": minimum, "maximum": maximum, "average": average}