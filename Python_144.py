def simplify(x, n):
    x_int = int(float(x.replace("/", "")) * float(n.replace("/", "")))
    return str(x) == str(x_int) + "/" + "1"