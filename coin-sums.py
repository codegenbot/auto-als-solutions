```
def coin_sums():
    n = int(input())
    coins = [25, 10, 5, 1]
    output = []
    
    for coin in coins:
        output.append(n // coin)
        n %= coin
    
    return output

print(*coin_sums(), sep='\n')