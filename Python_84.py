def solve(N):
    total = sum(int(x) for x in str(bin(N)[2:]))
    max_bin_len = len(bin(N)[2:])
    return ('0' * (max_bin_len - len(str(bin(total))[2:]))) + str(bin(total))[2:]