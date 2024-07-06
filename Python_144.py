def simplify(x, n):
    def lcm(a, b):
        return a * b // math.gcd(int(a.split('/')[0]), int(b.split('/')[0])) * int(b.split('/')[1]) // math.gcd(int(a.split('/')[0]), int(b.split('/')[1]))

    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))

    return (x_num*n_num) % lcm(x_den, n_den) == 0