```
def solve():
    N = int(input())  
    return "1" + ("0" * (N.bit_length() - 1)) + bin(N)[2:] if N % 2 == 0 else "0"