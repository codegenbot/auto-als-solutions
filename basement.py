```
def basement(arr):
    total = 0
    for i in range(len(arr)):
        running_total = sum(arr[:i+1])
        if running_total < 0:
            return i

print(basement([1])) 
print(basement([-100, 1]))
print(basement([2, -1, 100]))
print(basement([2, -95, 100]))
print(basement([2, -30, 5]))