```Python
def find_primes():
    num = int(input("Enter a number: "))
    primes = []
    
    for i in range(2, num + 1):
        is_prime = True
        
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
                
        if is_prime:
            primes.append(i)
    
    return primes

print(find_primes())