def find_zero(coeffs):
    a, b, c = coeffs[:3]
    d = coeffs[3:]
    roots = []
    for i in range(0, len(d), 2):
        temp = [a, 2 * a * d[i], c - (d[i + 1]) ** 2]
        try:
            root = (-temp[1] + math.sqrt((temp[1]) ** 2 - 4 * temp[0] * temp[2])) / (
                2 * temp[0]
            )
            roots.append(-d[i] / root)
        except (ZeroDivisionError, ValueError) as e:
            print(f"Failed to calculate a root: {e}")
    return roots