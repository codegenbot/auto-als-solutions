def solve(N):
    s = bin(sum(int(x) for x in str(bin(N)[2:])))
    max_len = len(format(max(1 << n for n in range(N.bit_length() + 1)), "b"))
    return s[2:].zfill(max_len)