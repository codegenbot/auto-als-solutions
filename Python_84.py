def solve(N):
    s = bin(sum(int(x) for x in str(bin(N)[2:])))
    max_len = len(format(1 << N.bit_length(), "b"))
    return s[2:].zfill(max_len)