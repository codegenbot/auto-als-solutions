def solve(input):
    if input == "t":
        return True
    elif input == "f":
        return False
    elif len(input) > 1:
        op = input[-1]
        a, b = input[:-1].split(op)
        if op == "|":
            return bool(a) or bool(b)
        else:
            return bool(a) and bool(b)