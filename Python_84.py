```
def solve(N):
    total = sum(int(x) for x in str(bin(N)[2:]))
    max_bin_len = bin((1 << N.bit_length()) - 1).count('1') + 1
    return ('0' * (max_bin_len - len(str(bin(total))[2:]))) + str(bin(total))[2:]