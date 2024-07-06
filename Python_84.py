def solve(N):
    if not isinstance(N, int):
        return "Error: Input must be an integer"
    binary = bin(N)[2:]
    result = ""
    for i in range(len(binary)):
        if binary[i] == "1":
            result += "*"
        else:
            result += "-"
    return result