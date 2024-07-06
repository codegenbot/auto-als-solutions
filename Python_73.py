```
def smallest_change(arr):
    n = len(arr)
    forward = arr[:]
    backward = arr[::-1]
    
    for i in range(n):
        if forward[i] != backward[n-i-1]:
            forward[i] = backward[n-i-1]

    return sum(1 for a, b in zip(forward, arr) if a != b)